def search_linear(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


if __name__ == '__main__':
    array = [4, 5, 9, 1, 8, 3, 6, 2, 7]
    print(f"Found at index: {search_linear(array, 8)}")
