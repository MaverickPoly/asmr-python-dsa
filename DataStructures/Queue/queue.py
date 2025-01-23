class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.size = 0
        self.last = None

    def add(self, value):
        if self.last is not None:  # Not Empty
            node = Node(value)
            node.prev = self.last
            self.last.next = node
            self.last = node
        else:  # Empty
            self.first = Node(value)
            self.last = self.first
        self.size += 1

    def peek(self):
        if self.is_empty():
            return None
        return self.first.value

    def pop(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        value = self.peek()
        if self.first == self.last:
            self.last, self.first = None, None
        else:
            self.first = self.first.next

        self.size -= 1
        return value

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __repr__(self):
        result = ""
        current = self.first
        while current is not None:
            result += f"{current.value} <- "
            current = current.next
        return result

    def __contains__(self, item):
        current = self.first
        while current is not None:
            if current.value == item:
                return True
            current = current.next
        return False


if __name__ == '__main__':
    queue = Queue()
    print(f"Queue empty: {queue.is_empty()}")
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.add(4)
    queue.add(5)
    print(queue.peek())
    print(queue)
    print(f"Queue empty: {queue.is_empty()}")

    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(4 in queue)
    print(1 in queue)
    print(f"Size: {len(queue)}")
    print(queue)
