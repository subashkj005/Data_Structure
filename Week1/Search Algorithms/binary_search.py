def binary_search(arr, value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    return -1


arr = [1, 2, 3, 4, 5]
print(binary_search(arr, 6))

"""

Binary search is a divide-and-conquer algorithm that is highly efficient for large datasets because 
it reduces the search space by half in each step. This makes it significantly faster than linear search
for sorted data.

The time complexity : O(log n)

"""
