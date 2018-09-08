from pybox.math import vec2d


def clamp(value, low, high):
    """Clamp a value between min/max and return the result.

    Example:
        >>> v0 = 35
        >>> vf = clamp(v0, 1, 10)
        >>> print(vf)
        10

    Args:
        value(mixed): value
        low(integer): lower limit
        high(integer): upper limit

    Return:
        mixed
    """

    true_min = min(low, high)
    true_max = max(low, high)

    return max(true_min, min(value, true_max))

def dot(a, b):
    """Calculate the dot product of two lists.

    Raises:
        AttributeError: Length of first list does not match length of second.

    Example:
        >>> l1 = [1, 2, 3]
        >>> l2 = [3, 4, 6]
        >>> product = dot(l1, l2)
        >>> print(product)
        29

    Args:
        a(*iterables): first list
        b(*iterables): second list

    Return:
        mixed
    """

    if len(a) != len(b):
        raise AttributeError('Length of first iterables does not match length of second.')

    return sum(i * j for i, j in zip(a, b))