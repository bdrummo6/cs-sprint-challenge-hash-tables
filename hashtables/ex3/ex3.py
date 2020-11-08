# function to determine which integers appear in all the arrays in a list of arrays
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    num_dict = {}

    # loop through each array in a list of arrays
    for arr in arrays:
        # loop through each integer in each array
        for num in arr:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

    # Create a list to hold the integers that appear in all arrays
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
