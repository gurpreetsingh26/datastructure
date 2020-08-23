
def min_squares(n):
    perfect_squares = []
    for i in range(1, int(n ** 0.5) + 1):
        if i * i <= n:
            perfect_squares.append(i * i)

    min_squares = [i for i in range(n + 1)]
    print(min_squares)
    for i in range(2, n + 1):
        for p in perfect_squares:
            min_squares[i] = min(min_squares[i], 1 + min_squares[i - p])
    print(min_squares)
    return min_squares[-1]


def test():
    """
    Test sorting
    :return:
    """
    n = 4

    if min_squares(n) == 1:
        print("Work as expected.")
    else:
        print("Check logic")

    n = 17

    if min_squares(n) == 2:
        print("Work as expected.")
    else:
        print("Check logic")


    if min_squares(18) == 2:
        print("Work as expeted")
    else:
        print("Check logic")

if __name__ == '__main__':
    test()

