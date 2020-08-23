
def sol1(arr, target):

    arr_sorted = sorted(arr)
    print(arr)
    #2 pointer approach
    i = 0;
    j = len(arr) - 1
    while i <= j:
        total = arr_sorted[i] + arr_sorted[j]
        if total == target:
            print("Found result")
            return arr_sorted[i], arr_sorted[j]
        elif total > target:
            j = j - 1
        else:
            i = i + 1

    print("No Result")
    return 0,0

def test():

    arr = [3, 2, 1, 5, 8, 6, 7, 4, 9, 10]

    first, second = sol1(arr, 17)

    if first == 7 and second == 10:
        print("Work as expected")
    else:
        print("Check logic")


if __name__ == '__main__':
    test()