from collections import deque


def tuple_replace(t, replace_at, value):
    return tuple(value if i == replace_at else v for i, v in enumerate(t))


def collides(bullet, position, x_offsets, y_offsets):
    x, y = position.x, position.y
    collides_x = x + x_offsets[0] < bullet.position.x < x + x_offsets[1]
    collides_y = y + y_offsets[0] < bullet.position.y < y + y_offsets[1]
    return collides_x and collides_y


def consume(iterator):
    """
    consumes an entire iterator, returning nothing.
    from the functools recipes.
    """
    deque(iterator, maxlen=0)
