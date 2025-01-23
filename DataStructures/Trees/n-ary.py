"""Each node n-amount of children."""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def traverse(self, node=None, level=0):
        if node is None:
            node = self.root
        print(" " * level + str(node.value))
        for child in node.children:
            self.traverse(child, level + 1)


if __name__ == '__main__':
    tree = Tree("Root")

    child1 = TreeNode("Child 1")
    child2 = TreeNode("Child 2")
    tree.root.add_child(child1)
    tree.root.add_child(child2)

    child1.add_child(TreeNode("Grandchild 1.1"))
    child1.add_child(TreeNode("Grandchild 1.2"))
    child2.add_child(TreeNode("Grandchild 2.1"))

    tree.traverse()

