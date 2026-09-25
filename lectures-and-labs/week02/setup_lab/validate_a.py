"""Basic email address validation."""


def validate_email(address: str) -> bool:
    """Return whether address has a valid basic email structure."""
    if not isinstance(address, str) or address != address.strip():
        return False
    if len(address) > 254 or address.count("@") != 1:
        return False

    local_part, domain = address.split("@")
    if not local_part or not domain or " " in address:
        return False
    if ".." in local_part or ".." in domain:
        return False
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False
    return True