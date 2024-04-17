def quicksort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    pivot = arr[n - 1]
    left = []
    right = []

    for i in range(n - 1):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quicksort(left) + [pivot] + quicksort(right)


new_arr = [2, 7, 5, 9, 6, 3, 8]
print(quicksort(new_arr))
