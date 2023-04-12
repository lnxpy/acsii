from acsii.constants.patterns import BASE_PATTERN


def serialize(density: int, typeset: str) -> str:
    """
    Serializes the density value converts it into a character.
    Args:
        typeset: ASCII characters type set
        density: pixel density value between 1 and 255

    Returns:
        a character corresponding to the density value
    """

    return BASE_PATTERN[typeset][density * len(BASE_PATTERN[typeset]) // 256]
