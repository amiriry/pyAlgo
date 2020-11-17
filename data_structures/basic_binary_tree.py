from typing import Optional
from random import randint
from sys import argv, exit

class Node:

    """A node has a variables that contains its data and option left or right nodes that relates to it"""
    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data

def display(tree: Optional[Node]) -> None:
    """Display the tree, reading from top to bottom left to right"""
    if tree:
        display(tree.left)
        print(tree.data)
        display(tree.right)


def tree_depth(tree: Optional[Node]) -> int:
    """ Calculate the depth of the tree, treating root as index 1 """
    return 1 + max(tree_depth(tree.left), tree_depth(tree.right)) if tree else 0

def is_full_binary_tree(tree: Node) -> bool:
    """Returns True if this is a full binary tree"""

    if not tree:
        return True
    if tree.left and tree.right:
        return is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
    else:
        return not tree.left and not tree.right

def usage():
    print("Usage:")
    print("\tManually:\npython3 basic_binary_tree.py\n   After running choose the amount of nodes or randomly with \'r\'")
    print("\tInside the command: basic_binary_tree r\n   This will choose the number of nodes and each value randomly ")

def main() -> None:
    if argv[1] == "help":
        usage()
        exit(0)
    number_of_nodes = int(input("Number of nodes you want in the tree:"))
    tree = Node(randint(0,100))
    for i in range(1, number_of_nodes):
            tree.insert(randint(0,100))

    print("number of nodes:", number_of_nodes)
    print("Is this a ful binary tree?", is_full_binary_tree(tree))
    print("The depth of the tree is:", tree_depth(tree))
    print("and the tree itself:")
    display(tree)

if __name__ == "__main__":
    main()
