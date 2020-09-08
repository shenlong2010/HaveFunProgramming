def all_equal(lst):
    """Checks if all elements in a list are equal.

    Returns:
        lst: list of numbers
    """
    return lst[1:] == lst[:-1]


# Testing
all_equal([1, 1, 1, 1])  # True
all_equal([1, 2, 3, 4, 5, 6])  # False
