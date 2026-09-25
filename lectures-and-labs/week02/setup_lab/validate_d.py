"""Email validation using a regex pattern."""

import re


def validate_email(address: str) -> bool:
    """Return whether address matches a basic email regex pattern."""
    if not isinstance(address, str) or len(address) > 254:
        return False

    pattern = r"^[^@]+@[^@]+\.[^@]+$"
    return bool(re.match(pattern, address))
