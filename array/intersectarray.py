
"""

Follow same for 6:
Divide and Conquer
solve for 3 and 3
then 2,1 and 2, 1
then 1,1,1 and 1,1,1

"""

def intersect(m,n):
    """
    Arrarys are sorted
    :param m:
    :param n:
    :return:
    """
    result = []
    i = j = 0
    while i < len(m) and j < len(n):

        if m[i] == n[j]:
            result.append(m[i])
            i = i + 1
            while i < len(n) and m[i] == m[i-1]:
                i = i + 1
            j = j + 1
            while j < len(n) and n[j] == n[j-1]:
                j = j + 1
        elif m[i] < n[j]:
            i = i + 1
        else:
            j = j + 1

    return result

def test():

    m = [5,10,40,50,70,80,90,100]
    n = [10,50,50,85,110]

    result = intersect(m, n)

    if result == [10,50]:
        print("Work as expected")
    else:
        print(result)
        print("Check logic")

if __name__ == "__main__":
    test()