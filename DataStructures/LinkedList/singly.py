class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Singly linked List
class Singly:
    def __init__(self):
        self.head = None
        self._size = 0

    # Push to the end
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self._size += 1

    # Remove the last element
    def pop(self):
        if self._size == 0:
            raise ValueError("The list is empty!")
        if self._size == 1:
            self.head = None
        res = self.get_last()
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        self._size -= 1
        return res

    # List contains a value?
    def __contains__(self, item):
        current = self.head
        while current is not None:
            if current.value == item:
                return True
            current = current.next
        return False

    # Get the value at a specific index
    def __getitem__(self, index):
        if index < 0 or index > self._size - 1:
            raise IndexError("Index out of range")

        current = self.head
        i = 0
        while current is not None:
            if i == index:
                return current.value
            current = current.next
            i += 1

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self._size += 1

    # Length of the list
    def __len__(self):
        return self._size

    # Return head
    def get_first(self):
        return self.peek()

    # Return last element in the list
    def get_last(self):
        if self._size == 0:
            return None
        current = self.head
        while current.next is not None:
            current = current.next
        return current.value

    # Index of a particular value
    def index_of(self, value):
        current = self.head
        i = 0
        while current is not None:
            if current.value == value:
                return i
            i += 1
            current = current.next
        return -1

    # Set item at index to smth
    def __setitem__(self, index, value):
        if self._size == 0:
            raise ValueError("The List is Empty!")
        if index < 0 or index > self._size - 1:
            raise IndexError("Index out of range!")
        current = self.head
        i = 0
        while current is not None:
            if i == index:
                current.value = value
                return
            i += 1
            current = current.next

    # Return head value
    def peek(self):
        if self._size == 0:
            raise ValueError("The list is empty!")
        return self.head.value

    # Remove first occurrence of a value
    def remove(self, value):
        if self._size == 0:
            raise ValueError("The list is empty!")
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return
            current = current.next
        raise ValueError("Value not found in the list!")

    # Set old value to new value
    def set(self, old_value, new_value):
        if self._size == 0:
            raise ValueError("The List is Empty!")
        current = self.head
        while current is not None:
            if current.value == old_value:
                current.value = new_value
                return
            current = current.next

    # Add a list of values to the end of the list
    def add_all(self, values):
        if self._size == 0:
            self.head = Node(values[0])
            current = self.head
            self._size += 1
            for value in values[1:]:
                node = Node(value)
                current.next = node
                current = node
                self._size += 1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            for value in values:
                node = Node(value)
                current.next = node
                current = node
                self._size += 1

    # Clear the linked list
    def clear(self):
        self.head = None
        self._size = 0

    # Is Empty
    def is_empty(self):
        return self._size == 0

    # Print
    def __repr__(self):
        current = self.head
        result = ""
        while current is not None:
            result += f"{current.value} -> "
            current = current.next
        return result


if __name__ == '__main__':
    ll = Singly()

    ll.append(4)
    ll.append(10)
    ll.append(12)
    ll.append(13)
    print(ll.pop())
    ll.prepend(3)
    ll.prepend(2)
    print(3 in ll)
    print(5 in ll)
    print(ll[1])
    print(ll[0])
    # print(ll[10])  # <- Error Raised
    print(f"Length: {len(ll)}")
    print(f"First: {ll.get_first()}")
    print(f"Last: {ll.get_last()}")
    print(f"Index of 4: {ll.index_of(4)}")
    print(f"Index of 5: {ll.index_of(5)}")
    ll[1] = 3.5
    ll[4] = 13
    # ll[15] = 14 # <- Index out of Range
    print(f"Peek: {ll.peek()}")
    print(ll)
    ll.remove(3.5)
    ll.set(10, 11)

    print("\nAfter removing:")
    print(ll)

    print(f"Is Empty: {ll.is_empty()}")
    ll.clear()
    print(f"Is Empty: {ll.is_empty()}")
    print(ll)

    # ll.append(1)
    # ll.append(2)
    ll.add_all([3, 4, 5])
    print(ll)
    print(len(ll))
