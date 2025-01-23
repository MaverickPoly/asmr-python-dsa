def binary_search(arr, target):
    start, end = 0, len(arr) - 1

    attempts = 0
    while start <= end:
        attempts += 1
        mid = start + (end - start) // 2
        if arr[mid] == target:
            print("Attempts: %d" % attempts)
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


if __name__ == '__main__':
    array = [i for i in range(1, 101)]
    print(f"Found at index: {binary_search(array, 51)}")
