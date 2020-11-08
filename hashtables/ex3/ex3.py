
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    num_dict = {}

    for arr in arrays:
        for num in arr:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

    result = []

    for arr in num_dict.items():
        if arr[1] == len(arrays):
            result.append(arr[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
