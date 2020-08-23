
def sort(arr):
    """
    Bubble sort
    :param arr:
    :return:
    """
    if len(arr) <= 1:
        return arr

    for i in range(len(arr)):
        for j in range(len(arr) -1, i, -1):
            if arr[j - 1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

    return arr


def test():
    """
    Test sorting
    :return:
    """
    arr = [2,1,8,0,-12,12]
    expected_arr = [-12, 0, 1, 2, 8, 12]
    actual_arr = sort(arr)

    if actual_arr == expected_arr:
        print("Works as expected")
    else:
        print(actual_arr)
        print("Check for logic")

if __name__ == '__main__':
    test()


