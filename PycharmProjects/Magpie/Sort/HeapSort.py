def heapify(array, size, root):

    left_index = root * 2 + 1
    right_index = left_index + 1
    largest = root
    if (left_index < size):
        if (array[largest] < array[left_index]):
            largest = left_index
    if (right_index < size):
        if (array[largest] < array[right_index]):
            largest = right_index
    if largest != root:
        array[largest] ,array[root] = array[root], array[largest]
        # heapify(array, size, largest)

def build_max_heap(array,size):

    for index in range(round(size/2-1),-1,-1):
        heapify(array, size, index)

    return array

def heap_sort(array):
    size = len(array)
    max_heap_array = build_max_heap(array,size)
    for index in range(size-1,-1,-1):
        max_heap_array[0], max_heap_array[index] = max_heap_array[index], max_heap_array[0]
        size -= 1
        build_max_heap(max_heap_array,size)

    return max_heap_array

if __name__ == '__main__':
    array = [2, 36, 7, 3, 98, 12, 33, 58, 4, 67, 9]
    array_order = heap_sort(array)
    print(array_order)