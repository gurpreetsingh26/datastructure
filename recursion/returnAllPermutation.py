
def sol(lst):

    def recursion(inp, idx, so_far, output):
        if idx == len(inp):
            output.append(so_far)
            return
        s = set()
        for i in range(idx, len(inp)):
            if inp[i] in s:
                continue
            s.add(inp[i])

            inp[i], inp[idx] = inp[idx], inp[i]
            new_so_far = so_far.copy()
            new_so_far.append(inp[idx])
            recursion(inp, idx + 1, new_so_far, output)
            inp[i], inp[idx] = inp[idx], inp[i]


    output = []
    initial = []
    recursion(lst, 0, initial, output)
    return output


def test():
    s = [1,2,3,3]
    result = sol(s)
    print(result)

    s = [1, 2, 3, 4]
    result = sol(s)
    print(result)

if __name__ == '__main__':
    test()
