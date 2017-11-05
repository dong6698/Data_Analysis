
def binary_search(key, array):
    print("Key number = ", key)
    print("Before sort = ", array)
    array.sort()
    print("After sort = ", array)
    lo = 0
    hi = len(array) - 1
    while lo <= hi:
        mid = int(lo + (hi - lo) / 2)
        if array[mid] < key:
            lo = mid + 1
        elif array[mid] > key:
            hi = mid - 1
        else:
            return mid


def main():
    key = 90
    array = [12, 45, 56, 17, 23, 78, 47, 60, 89, 90]
    result = binary_search(key, array)
    print("index = ", result)

if __name__ == '__main__':
    main()