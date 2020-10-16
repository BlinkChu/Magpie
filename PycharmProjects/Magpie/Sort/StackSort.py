
def stacksort(array):
    help = []
    while array:
        cur = array.pop()
        while help and help[-1] < cur:
            array.append(help.pop())
        help.append(cur)
    while help:
        stack.append(help.pop())


if __name__ == "__main__":
    stack = [3, 5, 4, 0, 1]
    stacksort(stack)
    print(stack)