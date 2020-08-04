
def sort_recursive(arr, n):
    """
    Insertion sort
    Top down
    Solution from n to n -2
    :param arr:
    :param n:
    :return:
    """
    if n <= 1:
        return

    sort_recursive(arr, n-1)

    j = n - 1
    element = arr[j]
    while j >= 1 and arr[j-1] > arr[j]:
        arr[j] = arr[j-1]
        j = j - 1
    arr[j] = element
    return arr

def sort_iterative(arr):
    """
    Insertion sort
    Top down
    Solution from n to n -2
    :param arr:
    :param n:
    :return:
    """
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        j = i
        element = arr[i]
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
    arr = [0,1,8,2,-12,12]

    sorted_arr = sort_recursive(arr, len(arr))
    if arr == sorted_arr:
        print "Recursive Works as expected"
    else:
        print sorted_arr
        print "Check for logic"

    sorted_arr = sort_iterative(arr)
    if arr == sorted_arr:
        print "Iterative Works as expected"
    else:
        print sorted_arr
        print "Check for logic"

if __name__ == '__main__':
    test()
