
def sort(arr):
    """
    Bubble sort
    :param arr:
    :return:
    """
    if len(arr) <= 1:
        return arr

    for i in range(len(arr)):
        for j in range(len(arr) -1, i + 1):
            if arr[j - 1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

    return arr


def test():
    """
    Test sorting
    :return:
    """
    arr = [2,1,8,0,-12,12]
    sorted_arr = sort(arr)

    if arr == sorted_arr:
        print "Works as expected"
    else:
        print sorted_arr
        print "Check for logic"

if __name__ == '__main__':
    test()


