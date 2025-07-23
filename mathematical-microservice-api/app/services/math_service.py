def compute_pow(base: int, exponent: int) -> int:
    """
    Compute the power of a base raised to an exponent.
    """
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    return base ** exponent
