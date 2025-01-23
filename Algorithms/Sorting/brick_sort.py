def brick_sort(arr):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(1, len(arr) - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        for i in range(0, len(arr) - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False


if __name__ == '__main__':
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(f"Original array: {array}")
    brick_sort(array)
    print(f"Sorted array: {array}")
