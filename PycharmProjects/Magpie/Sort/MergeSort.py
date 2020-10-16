def mergesort(array):
    if len(array) <= 1:
        return array
    num = round(len(array)/2)
    left = mergesort(array[:num])
    right = mergesort(array[num:])

    return merge(left, right)


def merge(left, right):
    r, l = 0, 0
    result = []
    while (r < len(right)) & (l < len(left)):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]

    return result

if __name__ == '__main__':
    list = [1, 5, 6, 12, 4, 7, 22, 43, 2, 15, 9]

    array_order = mergesort(list)
    print(array_order)