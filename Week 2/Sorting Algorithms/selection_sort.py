arr = [7, 3, 8, 36, 7, 35, 8, 4, 5]


def selection_sort(arr):
    n = len(arr)

    for current_index in range(n):
        min_index = current_index
        for search_index in range(current_index + 1, n):
            if arr[min_index] < arr[search_index]:
                min_index = search_index
        arr[current_index], arr[min_index] = arr[min_index], arr[current_index]

    print(arr)


selection_sort(arr)

"""
Selection sort is a sorting algorithm that selects the smallest or minimum element from an unsorted 
list in each iteration and places that element at the beginning of the unsorted list and after that 
starts from the first unsorted element.

Time Complexity	:- 
 
Best	O(n2)
Worst	O(n2)

Space Complexity	O(1)

"""
