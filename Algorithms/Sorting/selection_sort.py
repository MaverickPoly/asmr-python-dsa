def selection_sort(arr):
    """Iterate over the array, find the minimum value, and swap with it"""
    for i in range(len(arr) - 1):
        index = i  # Min Index
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]


if __name__ == '__main__':
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(f"Original: {array}")
    selection_sort(array)
    print(f"Sorted: {array}")
