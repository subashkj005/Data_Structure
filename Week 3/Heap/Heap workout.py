class PriorityQueue:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def add(self, priority, value):
        item = (priority, value)
        self.heap.append(item)
        self._percolate_up(len(self.heap)-1)

    def remove(self):
        if len(self.heap) == 0:
            raise IndexError("Priority queue is empty")
        self._swap(0, len(self.heap)-1)
        priority, value = self.heap.pop()
        self._percolate_down(0)
        return value

    def _percolate_up(self, index):
        parent_index = (index - 1) // 2
        while parent_index >= 0 and self.heap[parent_index][0] < self.heap[index][0]:
            self._swap(parent_index, index)
            index = parent_index
            parent_index = (index - 1) // 2

    def _percolate_down(self, index):
        child_index = 2 * index + 1
        while child_index < len(self.heap):
            if child_index + 1 < len(self.heap) and self.heap[child_index+1][0] > self.heap[child_index][0]:
                child_index += 1
            if self.heap[index][0] < self.heap[child_index][0]:
                self._swap(index, child_index)
                index = child_index
                child_index = 2 * index + 1
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def print_heap(self):
        n = len(self.heap)
        for i in range(n):
            print(self.heap[i], end=" ")


class Heap:
    def kth_smallest_max_heap(heap, k):
        n = len(heap)
        parent = (n - 1) // 2
        child = 2 * parent + 1
        heap[child] = -heap[child]
        for i in range(1, k):
            if 2 * parent + 2 < n:
                child = 2 * parent + 2
                if heap[child] > heap[child - 1]:
                    child -= 1
            parent = child // 2
            heap[child] = -heap[child]
        return -heap[0]


heap = PriorityQueue()
heap.add(2,5)
heap.add(1,5)
heap.add(0,5)
heap.add(3,5)
heap.add(1,6)
heap.print_heap()

