#!/bin/bash
# commitpush helper script - commits, pushes to both remotes (GitHub + GitLab),
# and creates/updates the GitHub PR and GitLab MR for the current dated branch.
#
# The commit message and PR/MR title+body are NOT generated here. They must be
# authored by whoever is driving this script (e.g. Claude reading the actual
# diff) and passed in explicitly, so they reflect the real intent of the
# change instead of a grep-based guess.
#
# Usage:
#   .commitpush-helper.sh -m "<commit message>" [-t "<pr/mr title>"] -b "<pr/mr body>"
#   .commitpush-helper.sh -m "<commit message>" [-t "<pr/mr title>"] -f <path-to-body-file>
#
#   -m   Commit message (required, first line is used as the summary everywhere a
#        short title is needed).
#   -t   PR/MR title (optional, defaults to the commit message).
#   -b   PR/MR body/description text (required unless -f is given).
#   -f   Path to a file containing the PR/MR body/description (use this for
#        multi-line descriptions instead of -b).

set -e

usage() {
    echo "Usage: $0 -m \"<commit message>\" [-t \"<pr/mr title>\"] (-b \"<body>\" | -f <body-file>)" >&2
    exit 1
}

COMMIT_MSG=""
PR_TITLE=""
PR_BODY=""
BODY_FILE=""

while getopts "m:t:b:f:h" opt; do
    case "$opt" in
        m) COMMIT_MSG="$OPTARG" ;;
        t) PR_TITLE="$OPTARG" ;;
        b) PR_BODY="$OPTARG" ;;
        f) BODY_FILE="$OPTARG" ;;
        h) usage ;;
        *) usage ;;
    esac
done

[ -z "$COMMIT_MSG" ] && usage

if [ -n "$BODY_FILE" ]; then
    [ -f "$BODY_FILE" ] || { echo "Body file not found: $BODY_FILE" >&2; exit 1; }
    PR_BODY=$(cat "$BODY_FILE")
fi

[ -z "$PR_BODY" ] && usage
[ -z "$PR_TITLE" ] && PR_TITLE="$COMMIT_MSG"

BRANCH_DATE=$(date +%d-%m-%Y)
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Switch to dated branch if needed
if [ "$CURRENT_BRANCH" != "$BRANCH_DATE" ]; then
    git checkout -b "$BRANCH_DATE" 2>/dev/null || git checkout "$BRANCH_DATE"
    echo "📌 Switched to branch: $BRANCH_DATE"
fi

# Stage all changes
git add -A

if git diff --cached --quiet; then
    echo "ℹ️ Nothing to commit"
    exit 0
fi

CHANGES_COUNT=$(git diff --cached --name-only | grep -c . || echo "0")
STATS=$(git diff --cached --shortstat | sed 's/^ *//')

echo "📝 Commit message: $COMMIT_MSG"
echo "📋 Changes: $CHANGES_COUNT file(s) | $STATS"

git commit -m "$COMMIT_MSG"

# Push to both remotes
git pushboth "$BRANCH_DATE"
echo "✅ Pushed to both remotes on branch: $BRANCH_DATE"

# Handle PR/MR creation and updates
echo "📋 Checking/creating PR & MR..."

# GitHub PR handling
if command -v gh >/dev/null 2>&1; then
    echo "   🔹 GitHub:"

    # Detect GitHub repo from remotes
    GH_REPO=$(git remote get-url github 2>/dev/null | sed 's|.*github.com[:/]||;s|\.git$||' || git remote get-url origin 2>/dev/null | grep github | sed 's|.*github.com[:/]||;s|\.git$||' || echo "")

    if [ -z "$GH_REPO" ]; then
        echo "      ℹ️ GitHub repo not configured in remotes"
    else
        # Check if PR exists - get full output for extraction
        PR_JSON=$(gh pr list --head "$BRANCH_DATE" --repo "$GH_REPO" --json number,title 2>/dev/null || echo "")

        if ! echo "$PR_JSON" | grep -q "number"; then
            # PR does not exist - Create new PR
            PR_URL=$(gh pr create --head "$BRANCH_DATE" --base main --title "$PR_TITLE" --body "$PR_BODY" --repo "$GH_REPO" 2>/dev/null | grep -o "https://[^[:space:]]*" || echo "")
            if [ -n "$PR_URL" ]; then
                echo "      ✅ PR created: $PR_URL"
            else
                echo "      ⚠️ Could not create PR"
            fi
        else
            # PR exists - update it
            PR_NUMBER=$(echo "$PR_JSON" | grep -o '"number":[0-9]*' | grep -o '[0-9]*' | head -1)
            if [ -n "$PR_NUMBER" ]; then
                # Update PR title and body
                gh pr edit "$PR_NUMBER" --title "$PR_TITLE" --body "$PR_BODY" --repo "$GH_REPO" 2>/dev/null && \
                    echo "      ✅ PR #$PR_NUMBER updated with new description" || \
                    echo "      ⚠️ Could not update PR"
            fi
        fi
    fi
else
    echo "   ℹ️ GitHub CLI (gh) not installed - skipping GitHub PR"
fi

# GitLab MR handling
if command -v glab >/dev/null 2>&1; then
    echo "   🔹 GitLab:"

    # Check if MR exists
    MR_JSON=$(glab mr list --source-branch "$BRANCH_DATE" -F json 2>/dev/null || echo "")

    if ! echo "$MR_JSON" | grep -q "iid"; then
        # MR does not exist - Create new MR
        MR_URL=$(glab mr create --source-branch "$BRANCH_DATE" --target-branch main --title "$PR_TITLE" --description "$PR_BODY" 2>/dev/null | grep -o "https://[^[:space:]]*" || echo "")
        if [ -n "$MR_URL" ]; then
            echo "      ✅ MR created: $MR_URL"
        else
            echo "      ⚠️ Could not create MR"
        fi
    else
        # MR exists - update it
        MR_IID=$(echo "$MR_JSON" | grep -o '"iid":[0-9]*' | grep -o '[0-9]*' | head -1)
        if [ -n "$MR_IID" ]; then
            # Update MR title and description
            glab mr update "$MR_IID" --title "$PR_TITLE" --description "$PR_BODY" 2>/dev/null && \
                echo "      ✅ MR !$MR_IID updated with new description" || \
                echo "      ⚠️ Could not update MR"
        fi
    fi
else
    echo "   ℹ️ GitLab CLI (glab) not installed - skipping GitLab MR"
fi

echo ""
echo "✨ Done! Branch: $BRANCH_DATE"
