import bs4 as _bs4
import requests as _requests


def _generate_url(month: str, day: int) -> str:
    """
    Generates a url for the given month and day.
    ::param month: The month to generate the url for.
    ::param day: The day to generate the url for.

    ::return: The generated url.
    """
    return f"https://www.onthisday.com/day/{month}/{day}"


def _get_page(url: str) -> str:
    """
    Gets the page at the given url.
    ::param url: The url to get the page from.

    ::return: The page at the given url.
    """
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup


def events_of_the_day(month: str, day: int) -> list[str]:
    """
    Gets the events of the day at the given month and day.
    ::param month: The month to get the events for.
    ::param day: The day to get the events for.

    ::return: The events of the day at the given month and day.
    """
    url = _generate_url(month, day)
    soup = _get_page(url)
    raw_events = soup.find_all(class_="event")
    events = [event.text for event in raw_events]
    return events
