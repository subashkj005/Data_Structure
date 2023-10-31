arr = [7, 3, 8, 36, 7, 35, 8, 4, 5]


def insertion_sort(arr):
    n = len(arr)
    for current_index in range(1, n):
        current_element = arr[current_index]
        previous_index = current_index - 1

        while previous_index >= 0 and current_element < arr[previous_index]:
            arr[previous_index + 1] = arr[previous_index]
            previous_index -= 1

        arr[previous_index + 1] = current_element

    print(arr)


insertion_sort(arr)

"""
Insertion sort is a sorting algorithm which sorts a list one element at a time. It starts by comparing the first two 
elements in the list and swapping them if they are in the wrong order. Then, it compares the third element to 
the sorted list and inserts it in the correct position. This process continues until the entire list is sorted.

Time Complexity	 :-

Best	O(n)
Worst	O(n2)

Space Complexity	O(1)

"""
