
def sol(n):

    def is_safe(so_far, row2, col2):

        for col1 in so_far:
            if col1 == col2:
                return False

        for row1 in range(0, len(so_far)):
            row_diff = abs(row2 - row1)
            col_diff = abs(col2 - so_far[row1])
            if row_diff == col_diff:
                return False

        return True

    def recursion(size, row, so_far, output):

        if size == row:
            output.append(so_far)
            return

        for i in range(0, size):
            if is_safe(so_far, row, i):
                new_so_far = so_far.copy()
                new_so_far.append(i)
                recursion(size, row + 1, new_so_far, output)

    result = []
    recursion(n, 0, [], result)
    return result


def test():

    result = sol(4)
    print(result)

    result = sol(3)
    print(result)

    result = sol(8)
    print(result)


if __name__ == '__main__':
    test()
