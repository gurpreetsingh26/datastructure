
def sol(s):

    def recursion(str1, index, so_far, result):

        if index == len(str1):
            result.append(so_far)
        else:
            curr_char = str1[index]
            if curr_char.isdigit() is True:
                recursion(str1, index + 1, so_far + curr_char, result)
            else:
                recursion(str1, index + 1, so_far + curr_char.lower(), result)
                recursion(str1, index + 1, so_far + curr_char.upper(), result)

    output = []
    recursion(s, 0, '', output)
    return output

def test():

    s = 't1D1'
    result = sol(s)
    print(result)

    s = '12345'
    result = sol(s)
    print(result)

    s = 'abc'
    result = sol(s)
    print(result)

if __name__ == '__main__':
    test()