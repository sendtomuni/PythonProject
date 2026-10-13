"""
claude
Don't generate lab for this
"""

import datetime as dt

class EventPlanner:
    def __init__(self, year):
        self.year = year
        self.events = {}

    def add_event(self, when, details):
        event_time = dt.datetime.strptime(when, '%d,%B %H:%M').replace(year=self.year)
        if event_time < dt.datetime.now():
            raise Exception("Invalid Date")
        else:
            self.events[event_time] = details

    def remove_event(self, when):
        event_time = dt.datetime.strptime(when, '%d,%B %H:%M').replace(year=self.year)
        return self.events.pop(event_time, None)

    def list_events(self):
        for when, details in self.events.items():
            print(f"event {details} is at {when.strftime('%d %B, %A %Y, %I:%M %p')}")


if __name__ == "__main__":
    def check(label, fn):
        try:
            result = fn()
            print(f"PASS  {label} -> {result!r}")
        except Exception as e:
            print(f"FAIL  {label} -> {type(e).__name__}: {e}")

    planner = EventPlanner(2026)

    # 1. add future events
    check("add future event 1", lambda: planner.add_event('25,December 10:00', 'Christmas party'))
    check("add future event 2", lambda: planner.add_event('31,December 22:30', 'New Year eve'))

    # 2. stored with correct year?
    check("stored keys have year 2026", lambda: all(k.year == 2026 for k in planner.events))
    check("events count == 2", lambda: len(planner.events) == 2)

    # 3. past date must be rejected
    check("past date raises", lambda: planner.add_event('01,January 09:00', 'Old event'))

    # 4. bad format must be rejected
    check("bad format raises", lambda: planner.add_event('2026-12-25 10:00', 'Wrong format'))

    # 5. list events
    check("list_events", planner.list_events)

    # 6. remove existing / missing event
    check("remove existing", lambda: planner.remove_event('25,December 10:00'))
    check("remove missing returns None", lambda: planner.remove_event('26,December 10:00'))
    check("events count == 1 after remove", lambda: len(planner.events) == 1)