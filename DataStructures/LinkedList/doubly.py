class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Doubly:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def remove(self, value):
        if self.is_empty():
            raise ValueError("The list is empty!")

        current = self.head
        while current is not None:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.size -= 1
                return
            current = current.next
        raise ValueError("Value not found in the list!")

    def display_forward(self):
        current = self.head
        while current is not None:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current is not None:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")


if __name__ == '__main__':
    dll = Doubly()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)

    dll.display_forward()
    dll.prepend(0)
    dll.display_forward()
    dll.remove(2)
    dll.remove(3)
    dll.display_backward()
