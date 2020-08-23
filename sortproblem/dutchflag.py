
def dutch_flag(arr):
    low = mid = 0
    high = len(arr) - 1

    while mid <= high:

        if arr[mid] == 1:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

def test():

    arr = [2,3,1,3,1,2,3]

    result = dutch_flag(arr)
    print(result)

if __name__ == "__main__":
    test()
