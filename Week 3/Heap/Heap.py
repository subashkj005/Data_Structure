# class Max_Heap:
#     def max_heapify(self, arr, n, i):
#         largest = i
#         left = 2 * i + 1
#         right = 2 * i + 2
#
#         # Check if left child is larger than root
#         if left < n and arr[left] > arr[largest]:
#             largest = left
#
#         # Check if right child is larger than largest
#         if right < n and arr[right] > arr[largest]:
#             largest = right
#
#         # If the largest element is not the root, swap them
#         if largest != i:
#             arr[i], arr[largest] = arr[largest], arr[i]
#             # Recursively max heapify the affected subtree
#             self.max_heapify(arr, n, largest)
#
#     def delete_max(self, arr):
#         n = len(arr)
#         # If the heap is empty, return None
#         if len(arr) == 0:
#             return None
#         # If the heap has only one element, remove and return it
#         if len(arr) == 1:
#             return arr.pop(0)
#         # If the heap has more than one element, remove the root (which is the maximum) and fix the heap property
#         else:
#             max = arr[0]
#             arr[0] = arr.pop()
#             self.max_heapify(arr, n, 0)
#             return max
#
#     def insert_node(self, arr, value):
#         arr.append(value)
#         i = len(arr)-1
#         # If the value is bigger than its parent, swap it with its parent until it reaches its correct position
#         while i > 0 and arr[(i-1)//2] < value:
#             arr[(i-1)//2], arr[i] = arr[i], arr[(i-1)//2]
#             i = (i-1)//2
#         return arr
#
#     def build_maxheap(self,arr):
#         n = len(arr)
#         # Starting from the last non-leaf node, perform max_heapify on each node to create a max heap
#         for i in range(n//2-1 ,-1 ,-1):
#             self.max_heapify(arr, n, i)
#
#     def print_heap(self, arr):
#         print(*arr)
#
#
# arr = [20,45,12,89,36,52,41,96,87]
# heap = Max_Heap()
# heap.build_maxheap(arr)
# print("Max heap:-")
# heap.print_heap(arr)
# print('deleted max value')
# heap.delete_max(arr)
# heap.print_heap(arr)
# print()
#
#
#
# class Min_Heap:
#     def min_heapify(self, arr, i):
#         left = 2*i+1
#         right = 2*i+2
#         n = len(arr)
#         min = i
#         # Find the minimum of the left and right children (if they exist) and the current node
#         if left < n and arr[left] < arr[i]:
#             min = left
#         if right < n and arr[right] < arr[min]:
#             min = right
#         # If the current node is not the minimum, swap it with the minimum child and continue recursively
#         if i != min:
#             arr[i], arr[min] = arr[min], arr[i]
#             self.min_heapify(arr, min)
#
#     def min_heapify(self, arr, n, i):
#         smallest = i
#         left = 2 * i + 1
#         right = 2 * i + 2
#
#         # Check if left child is smaller than root
#         if left < n and arr[left] < arr[smallest]:
#             smallest = left
#
#         # Check if right child is smaller than largest
#         if right < n and arr[right] < arr[smallest]:
#             smallest = right
#
#         # If the smallest element is not the root, swap them
#         if smallest != i:
#             arr[i], arr[smallest] = arr[smallest], arr[i]
#             # Recursively min heapify the affected subtree
#             self.min_heapify(arr, n, smallest)
#
#     def delete_min(self, arr):
#         # If the heap is empty, return None
#         if len(arr) == 0:
#             return None
#         # If the heap has only one element, remove and return it
#         if len(arr) == 1:
#             return arr.pop(0)
#         # If the heap has more than one element, remove the root (which is the minimum) and fix the heap property
#         else:
#             min = arr[0]
#             arr[0] = arr.pop()
#             self.min_heapify(arr,0)
#             return min
#
#     def insert_node(self, arr, value):
#         arr.append(value)
#         i = len(arr)-1
#         # If the value is smaller than its parent, swap it with its parent until it reaches its correct position
#         while i > 0 and arr[(i-1)//2] > arr[i]:
#             arr[(i-1)//2], arr[i] = arr[i], arr[(i-1)//2]
#             i = (i-1)//2
#         return arr
#
#     def build_minheap(self,arr):
#         n = len(arr)
#         # Starting from the last non-leaf node, perform min_heapify on each node to create a min heap
#         for i in range(n//2-1 ,-1 ,-1):
#             self.min_heapify(arr, n, i)
#
#     def print_heap(self, arr):
#         print(arr)
#
#
# arr = [20,45,12,89,36,52,41,96,87]
# heap = Min_Heap()
# heap.build_minheap(arr)
# print("Min Heap:-")
# heap.print_heap(arr)
#
# # class Heapsort:
# #     def max_heapify(self, arr, i):
# #         # if array starts with 0
# #         left = 2*i+1
# #         right = 2*i+2
# #         n = len(arr)
# #         max = i
# #         # Find the maximum of the left and right children (if they exist) and the current node
# #         if left < n and arr[left] > arr[i]:
# #             max = left
# #         if right < n and arr[right] > arr[max]:
# #             max = right
# #         # If the current node is not the maximum, swap it with the maximum child and continue recursively
# #         if i != max:
# #             arr[i], arr[max] = arr[max], arr[i]
# #             self.max_heapify(arr, max)
# #
# #
# #     def build_maxheap(self,arr):
# #         n = len(arr)
# #         # Starting from the last non-leaf node, perform max_heapify on each node to create a max heap
# #         for i in range(n//2-1 ,-1 ,-1):
# #             self.max_heapify(arr, i)
# #         return arr
# #
# #     def Heap_sort(self,arr):
# #         self.build_maxheap(arr)
# #         n = len(arr)
# #         for i in range(n-1,0,-1):
# #             arr[0], arr[i] = arr[i], arr[0]
# #             self.max_heapify(arr,0)
# #         return arr
# #
# #
# #     def print_heap(self, arr):
# #         print(arr)
# #
# #
# # print("Heap sort:-")
# # print(arr)
# # heap1 = Heapsort()
# # sort = heap1.Heap_sort(arr)
# # print(sort)

class HeapSort:

    def build_heap(self, arr):
        n = len(arr)
        # Start from the last non-leaf node and work backwards
        for i in range(n//2 - 1, -1, -1):
            # Perform max heapify on each node or heapify each non-leaf
            self.max_heapify(arr, n, i)

    def max_heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child is larger than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child is larger than largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If the largest element is not the root, swap them
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            # Recursively max heapify the affected subtree
            self.max_heapify(arr, n, largest)

    def heapsort(self, arr):
        n = len(arr)
        self.build_heap(arr)

        # Swap the root (largest element) with the last element, then max heapify the remaining heap and while
        # running loop each sorted one will be at the end of array
        for i in range(n-1, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.max_heapify(arr, i, 0)

        return arr

arr = [12, 36, 20, 87, 45, 52, 41, 96, 89]
print("Heap sort:-")
print(arr)
a = HeapSort()

print(a.heapsort(arr))