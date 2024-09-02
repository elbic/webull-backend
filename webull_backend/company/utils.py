"""
Module for handling cache operations and date manipulation.
"""

from datetime import date  # pylint: disable=E0401
from datetime import timedelta  # pylint: disable=E0401

from django.conf import settings  # pylint: disable=E0401
from django.core.cache import cache  # pylint: disable=E0401


def delete_cache(key_prefix: str) -> None:
    """
    Deletes all cache keys with the given prefix.

    Uses Django's built-in caching system to scan and delete cache keys
    that match the provided prefix. The keys are deleted in bulk, which can be more
    efficient than deleting each key individually.

    Args:
        key_prefix (str): The prefix of the cache keys to delete.
    """
    # Construct the pattern for matching cache keys using the given prefix and Django
    # settings
    keys_pattern = (
        f"views.decorators.cache.cache_*."
        f"{key_prefix}.*.{settings.LANGUAGE_CODE}.{settings.TIME_ZONE}"
    )

    # Delete all cache keys that match the constructed pattern
    cache.delete_pattern(keys_pattern)


def get_current_date() -> str:
    """
    Returns the current date in the format 'YYYY-MM-DD'.

    Uses the datetime.date.today() method to get the current date,
    then formats it into a string using strftime().
    """
    today = date.today()
    formatted_date = today.strftime("%Y-%m-%d")
    return formatted_date


def get_current_date_minus_n_days(days: int = 7) -> str:
    """
    Returns the current date minus n days in the format 'YYYY-MM-DD'.

    Args:
        days (int): The number of days to subtract from the current date.
            Defaults to 7.

    Returns:
        str: The past date in the format 'YYYY-MM-DD'.
    """
    today = date.today()
    past_date = today - timedelta(days=days)
    formatted_date = past_date.strftime("%Y-%m-%d")
    return formatted_date
