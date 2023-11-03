def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(linear_search(arr, 5))

"""
Linear search is straightforward and works for unsorted data, but it can be relatively slow for large datasets. 
 
The time complexity : O(n)

"""
