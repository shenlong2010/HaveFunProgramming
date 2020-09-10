def all_unique(lst):
    """Return true if all the values in a list are unique, 
    false otherwise.

    Args:
        lst (list): list of numbers

    Returns:
        boolean: return boolean if list are unique
    """
    return len(lst) == len(set(lst))

x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]
print(all_unique(x))
print(all_unique(y))
