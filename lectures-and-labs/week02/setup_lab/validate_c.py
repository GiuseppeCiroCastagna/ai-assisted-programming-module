"""Email address validation using a basic structural check."""


def validate_email(address: str) -> bool:
    """Return whether address has a basic, valid email structure."""
    if not isinstance(address, str) or address != address.strip():
        return False
    if not address or len(address) > 254 or address.count("@") != 1:
        return False

    local_part, domain = address.split("@")
    if not local_part or not domain or " " in address:
        return False
    if ".." in local_part or ".." in domain:
        return False
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False
    return True