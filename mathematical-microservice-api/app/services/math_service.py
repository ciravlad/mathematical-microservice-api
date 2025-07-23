def compute_pow(base: int, exponent: int) -> int:
    """
    Compute the power of a base raised to an exponent.
    """
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    return base ** exponent

def compute_factorial(number: int) -> int:
    if number < 0:
        raise ValueError("n must be non-negative")
    if number == 0 or number == 1:
        return 1
    result = 1
    for i in range (2, number + 1):
        result *= i
    return result


def compute_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b