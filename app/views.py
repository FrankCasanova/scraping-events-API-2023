from .services import get_all_events
from .services import get_day_events
from .services import get_month_events
from .services import get_today


async def all_events():
    """
    # [Show all events]
    This path operation shows all events in the app
    
    ### Returns a json with the all events in the app.
    """
    return get_all_events()


async def today_events():
    """
    # [Show all events for today]
    This path operation shows all events for today
   
    ### Returns a json with the all events for today.
    """
   
    return get_today()


async def month_events(month: str):
    """
    # [Show all events for a month]
    this path operation shows all events for a specific month
    ### Parameters:
    - month: str
    ### Returns a json with the all events for a specific month.
    """
    return get_month_events(month.lower())


async def day_events(month: str, day: int):
    """
    # [Show all events for a especific day]
    this path operation shows all events for a specific day
    ### Parameters:
    - month: str
    - day: int
    ### Returns a json with the all events for a specific day.
    """
    return get_day_events(month.lower(), day)
