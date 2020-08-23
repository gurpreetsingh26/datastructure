
def sol(n):

    def recursion(size, idx, so_far, open_counter, output):

        if idx >= size and open_counter == 0:
            output.append(so_far)
            return

        if idx >= size or open_counter > (size - idx):
            return

        recursion(size, idx + 1, so_far + "(", open_counter + 1, output)

        if open_counter > 0:
            recursion(size, idx + 1, so_far + ")", open_counter - 1, output)

    result = []
    recursion(2*n, 0, "", 0, result)
    return result


def sol1(n):

    def recursion(so_far, open_counter, close_counter, output):

        if open_counter > close_counter:
            return

        if open_counter == 0 and close_counter == 0:
            output.append(so_far)
            return

        if open_counter > 0:
            recursion(so_far + "(", open_counter - 1, close_counter, output)

        if close_counter > 0:
            recursion(so_far + ")", open_counter, close_counter - 1, output)

    result = []
    recursion("", n, n, result)
    return result


def test():

    result = sol(2)
    print(result)

    result = sol(3)
    print(result)

    result = sol(1)
    print(result)

    result = sol1(2)
    print(result)

    result = sol1(3)
    print(result)

    result = sol1(1)
    print(result)


if __name__ == '__main__':
    test()