class PriorityQueue:
    def __init__(self):
        self.heap = []

    def parent_index(self, i):
        return (i - 1) // 2

    def left_child_index(self, i):
        return 2 * i + 1

    def right_child_index(self, i):
        return 2 * i + 2

    def enqueue(self, value, priority):
        self.heap.append({'value': value, 'priority': priority})
        i = len(self.heap) - 1
        while i > 0:
            parent_index = self.parent_index(i)
            if self.heap[i]['priority'] < self.heap[parent_index]['priority']:
                self.heap[i], self.heap[parent_index] = self.heap[parent_index], self.heap[i]
                i = parent_index
            else:
                return

    def dequeue(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()['value']
        else:
            min_val = self.heap[0]['value']
            self.heap[0] = self.heap.pop()
            i = 0
            self.shift_down(i, len(self.heap))
            return min_val

    def shift_down(self, i, n):
        smallest = i
        left = self.left_child_index(i)
        right = self.right_child_index(i)

        if left < n and self.heap[left]['priority'] < self.heap[smallest]['priority']:
            smallest = left

        if right < n and self.heap[right]['priority'] < self.heap[smallest]['priority']:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.shift_down(smallest, n)

    def change_priority(self, heap, value, new_priority):
        for item in heap:
            if item['value'] == value:
                item['priority'] = new_priority
        heap.sort(key=lambda x: x['priority'])

    def level_order(self, heap):
        q = [0]
        list_str = ''
        while q:
            curr = q.pop(0)
            list_str += f"{heap[curr]['value']}\n"
            left = self.left_child_index(curr)
            right = self.right_child_index(curr)

            if left < len(heap):
                q.append(left)

            if right < len(heap):
                q.append(right)

        print(list_str)

    def get_min(self):
        return self.heap[0]['value']


pq = PriorityQueue()

# Priority Insertion
pq.enqueue("Task 1", 2)
pq.enqueue("Task 2", 1)
pq.enqueue("Task 3", 2)
pq.enqueue("Task 4", 1)

# Priority Deletion
# print(pq.dequeue()) # Task 2
# print(pq.dequeue()) # Task 4
# print(pq.dequeue()) # Task 1
# print(pq.dequeue()) # Task 3

# pq.level_order(pq.heap)
print(pq.get_min()) # Task 2

# Change Priority Of heap
pq.change_priority(pq.heap, "Task 3", 4)
pq.change_priority(pq.heap, "Task 2", 1)
pq.change_priority(pq.heap, "Task 1", 2)
pq.change_priority(pq.heap, "Task 4", 3)

print(pq.heap) # [{'value': 'Task 2', 'priority': 1}, {'value': 'Task 1', 'priority': 2}, {'value
