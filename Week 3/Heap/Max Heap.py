class Max_Heap:
    def __init__(self):
        self.arr = []

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

    def delete_max(self):
        arr = self.arr
        n = len(arr)
        # If the heap is empty, return None
        if len(arr) == 0:
            return None
        # If the heap has only one element, remove and return it
        if len(arr) == 1:
            return arr.pop(0)
        # If the heap has more than one element, remove the root (which is the maximum) and fix the heap property
        else:
            max = arr[0]
            arr[0] = arr.pop()
            self.max_heapify(arr, len(arr), 0)
            return max

    def insert_node(self, value):
        arr = self.arr
        arr.append(value)
        i = len(arr)-1
        # if the length is 1 or value is in correct position, the loop will not work
        # If the value is bigger than its parent, swap it with its parent until it reaches its correct position
        while i > 0 and arr[(i-1)//2] < value:
            arr[(i-1)//2], arr[i] = arr[i], arr[(i-1)//2]
            i = (i-1)//2
        return arr

    def build_maxheap(self):
        arr = self.arr
        n = len(arr)
        # Starting from the last non-leaf node, perform max_heapify on each node to create a max heap
        for i in range(n//2-1 ,-1 ,-1):
            self.max_heapify(arr, n, i)

    def print_heap(self):
        print(self.arr)

    # Building a heap from a array
    def build_heap(self,arr):
        n = len(arr)
        self.arr = arr
        # Start from the last non-leaf node and work backwards
        for i in range((n-1)//2,-1,-1):
            # Perform max heapify on each node or heapify each non-leaf
            self.max_heapify(self.arr,n,i)

    def heapsort(self):
        arr = self.arr
        n = len(arr)
        self.build_heap(arr)
        # Swap the root (largest element) with the last element, then max heapify the remaining heap and while
        # running loop each sorted one will be at the end of array
        for i in range(n-1,-1,-1):
            arr[0],arr[i] = arr[i], arr[0]
            self.max_heapify(arr,i,0)
        print("Heap sort :- ", *arr)





heap = Max_Heap()
heap.insert_node(96)
heap.insert_node(89)
heap.insert_node(52)
heap.insert_node(87)
heap.insert_node(36)
heap.insert_node(12)
heap.insert_node(41)
heap.insert_node(45)
heap.insert_node(20)
heap.build_maxheap()
print("Max heap:-")
heap.print_heap()
print('Deleted max value:- ')
heap.delete_max()
heap.print_heap()
heap.heapsort()
