
def sol(k, target):

    def recursion(idx, k, so_far, remainingSum, output):

        if idx == k and remainingSum == 0:
            output.append(so_far)
            return

        if idx == k or remainingSum < 0:
            return

        if idx == 6:
            return

        for i in range(1, 7):
            recursion(idx + 1, k, so_far + str(i), remainingSum - i, output)

    result = []
    recursion(0, k, '', target, result)
    return result

def test():

    result = sol(2,6)
    print(result)

    result = sol(2, 7)
    print(result)

    result = sol(3, 6)
    print(result)

if __name__ == '__main__':
    test()