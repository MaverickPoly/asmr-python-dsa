def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    left_arr = [0 for _ in range(n1)]
    right_arr = [0 for _ in range(n2)]

    for i in range(n1):
        left_arr[i] = arr[left + i]
    for j in range(n2):
        right_arr[j] = arr[mid + 1 + j]

    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


if __name__ == '__main__':
    array = [9, 5, 1, 8, 2, 3, 7, 6, 4, 0, 10]
    print(f"Original Array: {array}")
    merge_sort(array, 0, len(array) - 1)
    print(f"Sorted Array: {array}")
