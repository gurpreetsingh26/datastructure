
def binary_search(arr, target):
    """
    Assuming arrar is sorted
    :param arr:
    :param target:
    :return:
    """

    i = 0;
    j = len(arr) - 1
    while i <= j:
        mid = (i + j) // 2
        print(i)
        print(j)
        print(arr[mid])
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            j = mid
        else:
            i = mid

    return -1

def test():

    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    target = 7
    result = binary_search(arr, target)
    if result == target:
        print("Work as expected")
    else:
        print(result)
        print("Check logic")

if __name__ == "__main__":
    test()



