#Task-1

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def size(self):
        return len(self.items)

def reverse_sequence(input_sequence):
    stack = Stack()
    for char in input_sequence:
        stack.push(char)

    reversed_sequence = ""
    while not stack.is_empty():
        reversed_sequence += stack.pop()

    return reversed_sequence

input_sequence = input("Enter a sequence of characters: ")
reversed_result = reverse_sequence(input_sequence)
print("Reversed Sequence:", reversed_result)

#Task-2

def are_brackets_balanced(input_string):
    stack = Stack()
    opening_brackets = "({["
    closing_brackets = ")}]"
    brackets_map = {')': '(', '}': '{', ']': '['}

    for char in input_string:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty() or stack.pop() != brackets_map[char]:
                return False

    return stack.is_empty()

input_string = input("Enter a sequence with parentheses, braces, and curly brackets: ")
if are_brackets_balanced(input_string):
    print("Brackets are balanced.")
else:
    print("Brackets are not balanced.")

#Task-3

class Stack:

    def get_from_stack(self, element):
        if element in self.items:
            temp_stack = Stack()
            while not self.is_empty():
                item = self.pop()
                if item == element:
                    while not temp_stack.is_empty():
                        self.push(temp_stack.pop())
                    return element
                temp_stack.push(item)
            raise ValueError(f"{element} not found in the stack.")
        else:
            raise ValueError(f"{element} not found in the stack.")

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from an empty queue")

    def size(self):
        return len(self.items)

    def get_from_queue(self, element):
        if element in self.items:
            index = self.items.index(element)
            return self.items.pop(index)
        else:
            raise ValueError(f"{element} not found in the queue.")

#___
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.get_from_stack(2))

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.get_from_queue(20))

