def insertion_sort_algorithm(array, size):
    for i in range(1, size):
        value = array[i]
        hole = i
        while hole > 0 and array[hole-1] > value:
            array[hole] = array[hole-1]
            hole -= 1
        array[hole] = value


def main():
    array = [2, 7, 4, 1, 5, 3, 6]
    insertion_sort_algorithm(array, len(array))
    print(array)


if __name__ == '__main__':
    main()

# Time complexity is, Best case: O(n), Average case: O(n^2), Worst case: O(n^2)
