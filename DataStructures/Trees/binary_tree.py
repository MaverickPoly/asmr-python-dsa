"""Each Node has at most two children: left and right"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert_left(self, parent, value):
        if parent.left is None:
            parent.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = parent.left
            parent.left = new_node

    def insert_right(self, parent, value):
        if parent.right is None:
            parent.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = parent.right
            parent.right = new_node

    def traverse_inorder(self, node=None):
        """In-Order traversal: Left -> Root -> Right"""
        if node is None:
            node = self.root
        if node.left:
            self.traverse_inorder(node.left)
        print(node.value, end=" ")
        if node.right:
            self.traverse_inorder(node.right)

    def traverse_preorder(self, node=None):
        """Pre-order traversal: Root -> Left -> Right."""
        if node is None:
            node = self.root
        print(node.value, end=" ")
        if node.left:
            self.traverse_preorder(node.left)
        if node.right:
            self.traverse_preorder(node.right)

    def traverse_postorder(self, node=None):
        """Post-Order traversal: Left -> Right -> Root."""
        if node is None:
            node = self.root
        if node.left:
            self.traverse_postorder(node.left)
        if node.right:
            self.traverse_postorder(node.right)
        print(node.value, end=" ")


if __name__ == '__main__':
    bt = BinaryTree("Root")
    bt.insert_left(bt.root, "Left")
    bt.insert_right(bt.root, "Right")

    bt.insert_left(bt.root.left, "Left.Left")
    bt.insert_right(bt.root.left, "Left.Right")

    print("In-Order traversal:")
    bt.traverse_inorder()

    print("\n\nPre-Order Traversal:")
    bt.traverse_preorder()

    print("\n\nPost-Order Traversal:")
    bt.traverse_postorder()

