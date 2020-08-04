
def sort(arr, n):
    """
    Insertion sort
    :param arr:
    :param n:
    :return:
    """
    if n <= 1:
        return

    sort(arr, n-1)

    j = n - 1
    element = arr[j]
    while j >= 1 and arr[j-1] > arr[j]:
        arr[j] = arr[j-1]
        j = j - 1
    arr[j] = element
    return arr

def test():
    """
    Test sorting
    :return:
    """
    arr = [2,1,8,0,-12,12]
    sorted_arr = sort(arr, len(arr))

    if arr == sorted_arr:
        print "Works as expected"
    else:
        print sorted_arr
        print "Check for logic"

if __name__ == '__main__':
    test()
