def find_multiples(n, lim):
    """Returns a list of numbers in the arithmetic progression starting with 
    the given positive integer and up to the specified limit.

    Args:
        n (int): starting number
        lim (int): limit number

    Returns:
        list: list of numbers range from start to limit
    """
    return list(range(n, lim + 1, n))

print(find_multiples(5,25)) # 5, 10, 15, 20, 25