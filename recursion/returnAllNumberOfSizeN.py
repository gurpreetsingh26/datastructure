
def sol(size):

    def recursion(remaining_digits, so_far):

        if remaining_digits == 0:
            print(so_far)
        else:
            for i in range(0, 10):
                recursion(remaining_digits - 1, so_far + str(i))

    recursion(size, "")

def test():

    sol(2)
    sol(1)
    sol(3)

if __name__ == '__main__':
    test()
