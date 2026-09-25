"""Deliberately minimal email address validation."""


def validate_email(address: str) -> bool:
    """Return whether address contains an @ and a dot after it."""
    if not isinstance(address, str) or len(address) > 254:
        return False

    at_position = address.find("@")
    return at_position != -1 and "." in address[at_position + 1:]