"""Email address validation following the common dot-atom subset of RFC 5322."""

import re

_LOCAL_PART = re.compile(
    r"^[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*$"
)
_DOMAIN_LABEL = re.compile(r"^[A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?$")


def validate_email(address: str) -> bool:
    """Return whether address is a plausible, deliverable-looking email address."""
    if not isinstance(address, str) or len(address) > 254 or address.count("@") != 1:
        return False

    local_part, domain = address.split("@")
    if not 1 <= len(local_part) <= 64 or not _LOCAL_PART.match(local_part):
        return False

    labels = domain.split(".")
    if len(labels) < 2 or not all(_DOMAIN_LABEL.match(label) for label in labels):
        return False

    top_level = labels[-1]
    return len(top_level) >= 2 and top_level.isalpha()
