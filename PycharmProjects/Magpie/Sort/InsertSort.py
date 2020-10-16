def insertsort(array):
    for i in range(len(array)):
        for j in range(i, 0, -1):
            if array[j] <= array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array

if __name__ == '__main__':
    list = [1, 5, 6, 12, 4, 7, 22, 43, 2, 15, 9]

    array_order = insertsort(list)
    print(array_order)