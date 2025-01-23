def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    array = [7, 8, 4, 5, 3, 9, 6, 2, 1, 10]
    bubble_sort(array)
    print(array)

