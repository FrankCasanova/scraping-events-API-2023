from .services import get_all_events
from .services import get_day_events
from .services import get_month_events
from .services import get_today


async def all_events():
    """
    return all events

    ::return: dict
    """
    return get_all_events()


async def today_events():
    """_summary_
    return events for today

    ::return: dict
    """
    return get_today()


async def month_events(month: str):
    """
    return events for a specific month

    : : param month: str
    : : return: dict
    """
    return get_month_events(month.lower())


async def day_events(month: str, day: int):
    """
    return events for a specific day

    : : param month: str
    : : param day: int
    : : return: dict
    """
    return get_day_events(month.lower(), day)
