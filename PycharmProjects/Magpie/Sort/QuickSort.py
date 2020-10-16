# quick sort
def quicksort_1(array, start, end):
    while start >= end:
        return array
    tmp = array[start]
    j = end
    i = start
    while i < j:
        while (i < j) and array[j] >= tmp:
            j -= 1
        else:
            array[i] = array[j]

        while (i < j) and array[i] <= tmp:
            i += 1
        else:
            array[j] = array[i]

    array[i] = tmp
    quicksort_1(array, start, i-1)
    quicksort_1(array, i+1, end)

    return array
if __name__ == '__main__':
    list = [1, 5, 6, 12, 4, 7, 22, 43, 2, 15, 9]

    array_order = quicksort_1(list, 0, len(list)-1)
    print(array_order)