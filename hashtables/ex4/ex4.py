def has_negatives(a):
    """
    YOUR CODE HERE
    """
    num_dict = {}

    result = []

    for num in a:
        num_dict[num] = None

    for num in a:
        if num* -1 in num_dict and num > 0:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
