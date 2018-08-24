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

def computeAABB(cx, cy, w, h, angle):
    # calculate rotated vertices of each corner
    v1 = vec2d.Vec2d(-w/2, -h/2).rotate(angle)
    v2 = vec2d.Vec2d( w/2, -h/2).rotate(angle)
    v3 = vec2d.Vec2d( w/2,  h/2).rotate(angle)
    v4 = vec2d.Vec2d(-w/2,  h/2).rotate(angle)

    x1, y1 = v1.unpack()
    x2, y2 = v2.unpack()
    x3, y3 = v3.unpack()
    x4, y4 = v4.unpack()

    # extents of final AABB
    ex = max(x1, x2, x3, x4)
    ey = max(y1, y2, y3, y4)

    # finally get new top/right and bottom/right coordinates
    x1 = cx - ex
    x2 = cx + ex
    y1 = cy - ey
    y2 = cy + ey

    return x1, y1, x2, y2

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