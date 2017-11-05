def bubble_sort_algorithm(array, size):
    for k in range(size-1):
        flag = True
        for i in range(size-k-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                flag = False
        if flag is True:
            break


def main():
    array = [2, 7, 4, 1, 5, 3, 6]
    bubble_sort_algorithm(array, len(array))
    print(array)


if __name__ == '__main__':
    main()

# Time complexity is, Best case: O(n), Average case: O(n^2), Worst case: O(n^2)
