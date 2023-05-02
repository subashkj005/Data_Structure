class Min_heap:
    def __init__(self):
        self.arr = []

    def min_heapify(self, n, i):
        arr = self.arr
        min = i
        left = 2*i+1
        right = 2*i+2
        if left < n and arr[left] < arr[i]:
            min = left
        if right < n and arr[right] < arr[min]:
            min = right
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            self.min_heapify(n, min)

    def insert_heap(self, value):
        arr = self.arr
        arr.append(value)
        i = len(arr)-1
        while i > 0 and value < arr[(i-1)//2]:
            arr[i], arr[(i-1)//2] = arr[(i-1)//2], arr[i]
            i = (i-1)//2
        return arr

    def delete_min(self):
        arr = self.arr
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return arr.pop()
        else:
            min = arr[0]
            arr[0] = arr.pop()
            self.min_heapify(len(arr), 0)
        return min

    def build_heap_min(self, arr):
        self.arr = arr
        n = len(arr)
        for i in range((n-1)//2, -1, -1):
            self.min_heapify(n, i)

    def heapsort(self):
        arr = self.arr
        n = len(arr)
        self.build_heap_min(arr)
        for i in range(n-1,-1,-1):
            arr[0], arr[i] = arr[i], arr[0]
            self.min_heapify(i, 0)
        print(*arr)

    def print_heap(self):
        print(*self.arr)


heap = Min_heap()
heap.insert_heap(96)
heap.insert_heap(89)
heap.insert_heap(52)
heap.insert_heap(87)
heap.insert_heap(36)
heap.insert_heap(12)
heap.insert_heap(41)
heap.insert_heap(45)
heap.insert_heap(20)
heap.print_heap()
heap.delete_min()
heap.print_heap()
heap.heapsort()