from fastapi import APIRouter

from .views import all_events
from .views import day_events
from .views import month_events
from .views import today_events

router = APIRouter(prefix="/api")

router.add_api_route(
    "/events",
    all_events,
    methods=["GET"],
    status_code=200,
    summary="Get all events",
    tags=["events"],
)

router.add_api_route(
    "/events/today",
    today_events,
    methods=["GET"],
    status_code=200,
    summary="Get events for today",
    tags=["events"],
)

router.add_api_route(
    "/events/{month}",
    month_events,
    methods=["GET"],
    status_code=200,
    summary="Get events for a specific month",
    tags=["events"],
)

router.add_api_route(
    "/events/{month}/{day}",
    day_events,
    methods=["GET"],
    status_code=200,
    summary="Get events for a specific day",
    tags=["events"],
)
