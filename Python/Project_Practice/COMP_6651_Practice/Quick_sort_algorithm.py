def partition(array, start_index, end_index):
    pivot = array[end_index]
    p_index = start_index
    for i in range(start_index, end_index):
        if array[i] <= pivot:
            array[i], array[p_index] = array[p_index], array[i]
            p_index += 1
    array[p_index], array[end_index] = array[end_index], array[p_index]
    return p_index


def quick_sort_algorithm(array, start_index, end_index):
    if start_index < end_index:
        partition_index = partition(array, start_index, end_index)
        quick_sort_algorithm(array, 0, partition_index-1)
        quick_sort_algorithm(array,partition_index + 1, end_index)


def main():
    array = [2, 7, 4, 1, 5, 3, 6]
    quick_sort_algorithm(array, 0, len(array)-1)
    print(array)


if __name__ == '__main__':
    main()