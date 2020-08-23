
from random import randint


def sort(arr):

    def partition(array, start_index, end_index, pivot_index):

        pivot = array[pivot_index]
        print("start: {0}, {1}".format(start_index, arr[start_index]))
        print("end: {0}, {1}".format(end_index, arr[end_index]))
        print("pivot: {0}, {1}".format(pivot_index, arr[pivot_index]))

        left = start_index
        right = end_index

        array[right], array[pivot_index] = array[pivot_index], array[right]

        while left <= right:
            print("left: {0}, {1}".format(left, arr[left]))
            print("right: {0}, {1}".format(right, arr[right]))
            if array[left] < pivot:
                left = left + 1
            elif array[right] > pivot:
                right = right - 1
            else:
                array[left], array[right] = array[right], array[left]
            print(array)




    def quick_sort(array, start_index, end_index):
        if start_index >= end_index:
            return

        pivot_index = randint(start_index, end_index)
        partition(array, start_index, end_index, pivot_index)
        quick_sort(array, start_index, pivot_index - 1)
        quick_sort(array, pivot_index + 1, end_index)

    quick_sort(arr, 0, len(arr) - 1)
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
