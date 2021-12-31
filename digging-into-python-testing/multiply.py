"""multiply.py"""


def multiply_int(x: int, y: int) -> int:
    """
    >>> multiply_int(10, 1)
    10
    """
    return x * y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
