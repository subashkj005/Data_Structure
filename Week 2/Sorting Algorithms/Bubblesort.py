arr = [3, 5, 3, 6, 7, 83, 4, 2, 6]


def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True
        if not swapped:
            break

    print(arr)


bubble_sort(arr)

"""

Bubble sort is a sorting algorithm that compares two adjacent elements and swaps
them until they are in the intended order.

Time Complexity :- 

Worst case : O(n^2) 
Best case : O(n) 

Space complexity : O(1)

"""
