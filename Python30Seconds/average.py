def average(*args):
    """Return the average of two or more numbers

    Returns:
        float: the average number
    """
    return sum(args, 0.0) / len(args)

print(average(*[1, 2, 3])) # 2.0
print(average(1, 2, 3)) # 2.0