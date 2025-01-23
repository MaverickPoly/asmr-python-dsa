def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i


def quick_sort(arr, start, end):
    if start < end:
        part = partition(arr, start, end)
        quick_sort(arr, start, part - 1)
        quick_sort(arr, part + 1, end)


if __name__ == '__main__':
    array = [9, 8, 1, 2, 3, 4, 7, 6, 5, 10, 0]
    print(f"Original: {array}")
    quick_sort(array, 0, len(array) - 1)
    print(f"Sorted: {array}")
