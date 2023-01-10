from types import SimpleNamespace


FOO = 17

def add_one(x):
    return x + 1


def add_foo(x):
    return x + FOO


def divide_things(x, y):
    return x / y


def add_things(x, y=1, z=2):
    sum = x + y + z
    return sum


def first_two(array):
    return array[0], array[1]


def nicer_first_two(array):
    """This is the docstring

    :param array: Array to pull first 2 items from
    :type array: list
    """
    result = SimpleNamespace(
        first=array[0],
        second=array[1],
    )
    return result


nicer_first_two()