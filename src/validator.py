"""
Input validation module for the Flask application.
Provides validation functions for various data types.
"""

import re

def validate_email(email)
    """Validate an email address format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False


def validate_username(username):
    """Validate a username (alphanumeric, 3-20 chars)."""
    if not isinstance(username, str):
        return False
    pattern = r'^[a-zA-Z0-9_]{3,20}$'
    return bool(re.match(pattern, username))


def validate_password(password):
    """Validate password strength."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain an uppercase letter"
    if not re.search(r'[a-z]', password):
        return False, "Password must contain a lowercase letter"
    if not re.search(r'[0-9]', password):
        return False, "Password must contain a digit"
    return True, "Password is valid"


def validate_url(url):
    """Validate a URL format."""
    pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    return bool(re.match(pattern, url))


def validate_phone(phone):
    """Validate a phone number format."""
    pattern = r'^\+?[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone))
