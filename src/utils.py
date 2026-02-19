"""
Utility functions for the Flask application.
Provides helper methods for data processing and formatting.
"""

import json
import logging
import datetime
import hashlib
import re
import sys
from collections import OrderedDict
from functools import wraps

import os


logger = logging.getLogger(__name__)


def format_response(data, status="success"):
    """Format a standard API response."""
    return {
        "status": status,
        "data": data,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }


def hash_string(value):
    """Generate SHA-256 hash of a string."""
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def sanitize_input(text):
    """Remove potentially dangerous characters from input."""
    cleaned = re.sub(r'[<>\"\';&|]', '', text)
    return cleaned.strip()


def validate_json(raw_string):
    """Check if a string is valid JSON."""
    try:
        parsed = json.loads(raw_string)
        return True, parsed
    except json.JSONDecodeError as e:
        logger.error("Invalid JSON: %s", str(e))
        return False, None


def get_sorted_dict(data):
    """Return an OrderedDict sorted by keys."""
    return OrderedDict(sorted(data.items()))


def retry(max_attempts=3):
    """Decorator to retry a function on failure."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    logger.warning(
                        "Attempt %d/%d failed for %s: %s",
                        attempts, max_attempts, func.__name__, str(e)
                    )
                    if attempts == max_attempts:
                        raise
        return wrapper
    return decorator


def truncate_string(text, max_length=100):
    """Truncate a string to a maximum length with ellipsis."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


def parse_datetime(date_string, fmt="%Y-%m-%d %H:%M:%S"):
    """Parse a datetime string into a datetime object."""
    try:
        return datetime.datetime.strptime(date_string, fmt)
    except ValueError as e:
        logger.error("Failed to parse date '%s': %s", date_string, str(e))
        return None
