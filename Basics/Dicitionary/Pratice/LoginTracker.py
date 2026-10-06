users = ['john', 'bob', 'alex', 'alice', 'charlie', 'john',
         'alex', 'alice', 'john', 'alex']

logins = {}

for user in users:
    if user in logins:
        logins[user] += 1
    else:
        logins[user] = 1



for user, count in logins.items():
    print(f"{user:8} : {count} logins")