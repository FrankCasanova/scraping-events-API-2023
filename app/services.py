import datetime as _dt
import json as _json
from typing import Dict
from typing import List


def get_all_events() -> Dict[str, Dict[str, List[str]]]:
    with open("scraper/events.json", encoding="utf-8") as f:
        events = _json.load(f)

    return events


def get_month_events(month: str) -> Dict[str, Dict[str, List[str]]]:
    try:
        events = get_all_events()
        return events[month]
    except KeyError:
        return "This month doesn't exist"


def get_day_events(month: str, day: int) -> list:
    try:
        events = get_month_events(month)
        return events[str(day)]
    except KeyError:
        return "This day doesn't exist"


def get_today() -> list:
    today = _dt.date.today()
    print(today)
    month = today.strftime("%B").lower()
    print(month)
    day = str(today.day)
    print(day)
    return get_day_events(month, day)
