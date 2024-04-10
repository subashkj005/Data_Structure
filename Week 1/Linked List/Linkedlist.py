class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_linked_list(self):
        if not self.head:
            return 'Empty'
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def delete_node(self, data):
        if not self.head:
            return 'Empty'

        current = self.head
        prev = None

        while current:
            if current.value == data:
                if not prev:
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = None
                return
            prev = current
            current = current.next

    def pop(self):
        if not self.head:
            return
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        return 1

    def reverse_linkedlist(self):
        if not self.head:
            return
        current = self.head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


node = Linkedlist()
node.append(10)
node.append(15)
node.append(20)

node.print_linked_list()

# node.delete_node(15)
# print('node deleted')
# node.pop()
# node.print_linked_list()
print('__________________')
node.reverse_linkedlist()
node.print_linked_list()
