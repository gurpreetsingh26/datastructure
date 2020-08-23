
def sort(arr):
    """
    Merge sort
    :param arr:
    :param n:
    :return:
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = sort(arr[0:mid])
    right = sort(arr[mid:len(arr)])

    return merge(left, right)


def merge(left, right):
    i = j = 0
    aux = [0] * (len(left) + len(right))
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            aux[i + j] = left[i]
            i = i + 1
        else:
            aux[i + j] = right[j]
            j = j + 1

    while i < len(left):
        aux[i + j] = left[i]
        i = i + 1

    while j < len(right):
        aux[i + j] = right[j]
        j = j + 1
    return aux


def test():
    """
    Test sorting
    :return:
    """
    arr = [2, 1, 8, 0, -12, 12]
    expected_arr = [-12, 0, 1, 2, 8, 12]
    actual_arr = sort(arr)
    if expected_arr == actual_arr:
        print("Works as expected")
    else:
        print(sort)
        print("Check for logic")


if __name__ == '__main__':
    test()
