def insertion_sort(arr):
    for i in range(len(arr)):
        val = arr[i]
        j = i - 1

        while j >= 0 and val < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = val


if __name__ == '__main__':
    array = [8, 9, 3, 2, 1, 0, 4, 5, 6, 7]
    print("Original array:", array)
    insertion_sort(array)
    print(array)
