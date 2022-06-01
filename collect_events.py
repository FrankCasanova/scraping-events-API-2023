import datetime as _dt
import json as _json
from typing import Dict
from typing import Iterator

import scraper as _scraper


def _date_range(start_date: _dt.date, end_date: _dt.date) -> Iterator[_dt.date]:
    """
    A generator that yields dates between start_date and end_date.
    ::param start_date: The first date to yield.
    ::param end_date: The last date to yield.
    """
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += _dt.timedelta(days=1)


def create_events_dict() -> Dict[str, Dict[str, list[str]]]:
    """
    A function that creates a dictionary of events.
    """
    events = dict()
    start_date = _dt.date(2021, 1, 1)
    end_date = _dt.date(2021, 12, 31)

    for date in _date_range(start_date, end_date):
        month = date.strftime("%B").lower()
        if month not in events:
            events[month] = dict()

        events[month][date.day] = _scraper.events_of_the_day(month, date.day)

    return events


if __name__ == "__main__":
    events = create_events_dict()
    with open("events.json", "w", encoding="utf-8") as f:
        _json.dump(events, f, ensure_ascii=False, indent=4)
