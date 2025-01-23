class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        if self.is_empty():
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        value = self.peek()
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None

    def __contains__(self, item):
        current = self.top
        while current is not None:
            if current.value == item:
                return True
            current = current.next
        return False

    def __len__(self):
        size = 0
        current = self.top
        while current is not None:
            size += 1
            current = current.next
        return size

    def __repr__(self):
        res = ""
        current = self.top
        while current is not None:
            res += f"---- {current.value} ----\n"
            current = current.next
        return res


if __name__ == '__main__':
    stack = Stack()
    print(f"\tIs Empty: {stack.is_empty()}")
    print("Size:", len(stack))
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.peek())

    print(stack)
    print(f"\tIs Empty: {stack.is_empty()}")
    print("Size:", len(stack))
    print(stack.pop())
    print(stack.pop())
    print(3 in stack)
    print(2 in stack)
    print(stack)
