#Task-1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def index(self, item):
        current = self.head
        index = 0
        while current:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError(f"{item} not found in the list")

    def pop(self, pos=None):
        if self.is_empty():
            raise IndexError("Pop from an empty list")

        if pos is None:
            if self.head.next is None:
                popped_item = self.head.data
                self.head = None
                return popped_item

            current = self.head
            while current.next.next:
                current = current.next
            popped_item = current.next.data
            current.next = None
            return popped_item
        else:
            if pos < 0:
                raise ValueError("Negative position not allowed")
            if pos == 0:
                popped_item = self.head.data
                self.head = self.head.next
                return popped_item

            current = self.head
            prev = None
            index = 0
            while current and index < pos:
                prev = current
                current = current.next
                index += 1

            if not current:
                raise IndexError("Index out of range")

            popped_item = current.data
            prev.next = current.next
            return popped_item

    def insert(self, pos, item):
        if pos < 0:
            raise ValueError("Negative position not allowed")

        new_node = Node(item)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            index = 0
            while current and index < pos:
                prev = current
                current = current.next
                index += 1
            if not current and index < pos:
                raise IndexError("Index out of range")
            prev.next = new_node
            new_node.next = current

    def slice(self, start, stop):
        if start < 0 or stop < 0:
            raise ValueError("Negative start or stop position not allowed")
        if start >= stop:
            return UnorderedList()

        current = self.head
        result = UnorderedList()
        index = 0
        while current and index < stop:
            if index >= start:
                result.append(current.data)
            current = current.next
            index += 1
        return result



my_list = UnorderedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
print("Original List:", [my_list.index(x) for x in [1, 2, 3, 4]])
print("Popped item:", my_list.pop())  # Output: 4
my_list.insert(1, 5)
print("List after insert:", [my_list.index(x) for x in [1, 5, 2, 3]])
sliced_list = my_list.slice(1, 3)
print("Sliced List:", [sliced_list.index(x) for x in [5, 2]])

#Task-2

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        popped_item = self.head.data
        self.head = self.head.next
        return popped_item

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Popped item:", stack.pop())

#Task-3

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue.")
        popped_item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return popped_item

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Dequeued item:", queue.dequeue())


