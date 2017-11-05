def selection_sort_algorithm(array, size):
    for i in range(size-1):                 # i = 0, 1, 2, 3, 4, 5  size = 6
        iMin = i
        # Find the min within the array
        for j in range(i+1, size):
            if array[j] < array[iMin]:
                iMin = j
        # Exchange the min with index i
        temp = array[i]
        array[i] = array[iMin]
        array[iMin] = temp


def main():
    array = [2, 7, 4, 1, 5, 3, 6]
    selection_sort_algorithm(array, len(array))
    print(array)


if __name__ == '__main__':
    main()

# Time complexity is O(n^2)

