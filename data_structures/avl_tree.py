"""
Auto-balanced binary tree
"""

import random
import math

class my_queue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def push(self, data):
        self.data.append(data)
        self.tail = self.tail + 1

    def pop(self):
        to_return = self.data[self.head]
        self.head = self.head + 1
        return to_return

    def count(self):
        return self.tail - self.head

    def print(self):
        print(self.data)
        print("*****************************")
        print(self.data[self.head : self.tail])

class my_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_height(self):
        return self.height

    def set_left(self, node):
        self.left = node
        return

    def set_right(self, node):
        self.right = node
        return

    def set_data(self, data):
        self.data = data
        return

    def set_height(self, height):
        self.height = height
        return

def get_height(node):
    if node is None:
        return  0
    return node.get_height()

def max_between(a,b):
    if a > b:
        return a
    return b

def right_rotation(node):
    print("The node that is unbalanced:", node.get_data())
    to_return = node.get_left()
    node.set_left(to_return.get_right()) # The switch - the move to other side of the tree
    to_return.set_right(node)
    h1 = max_between(get_height(node.get_right()), get_height(node.get_left())) + 1
    node.set_height(h1)
    h2 = max_between(get_height(to_return.get_right()), get_height(to_return.get_left())) + 1
    to_return.set_height(h2)
    return to_return

def left_rotation(node):
    print("right rotation node:", node.get_data())
    to_return = node.get_right()
    node.set_right(to_return.get_left())
    to_return.set_left(node)
    h1 = max_between(get_height(node.get_right()), get_height(node.get_left())) + 1
    node.set_height(h1)
    h2 = max_between(get_height(to_return.get_right()), get_height(to_return.get_left())) + 1
    to_return.set_height(h2)
    return to_return

def left_right_rotation(node):
    left_child = node.get_left()
    node.set_left(left_rotation(left_child)) # The first rotation that keeps the tree not balanced
    return right_rotation(node) # The rotation that balances the tree

def right_left_rotation(node):
    right_child = node.get_right()
    node.set_right(right_rotation(right_child))
    return left_rotation(node)

def insert_node(add_node, data):
    if add_node is None:
        return my_node(data)
    if data < add_node.get_data():
        add_node.set_left(insert_node(add_node.get_left(), data))
        if get_height(add_node.get_left()) - get_height(add_node.get_right()) == 2:
            left_child = add_node.get_left()
            if data < left_child.get_data():
                add_node = right_rotation(add_node)
            else:
                add_node = left_right_rotation(add_node)
    else: # data <= add_node.get_data()
        add_node.set_right(insert_node(add_node.get_right(), data))
        if get_height(add_node.get_right()) - get_height(add_node.get_left()) == 2:
            right_child = add_node.get_right()
            if data < right_child.get_data():
                add_node = right_left_rotation(add_node)
            else:
                add_node = left_rotation(add_node)
    h1 = max_between(get_height(add_node.get_right()), get_height(add_node.get_left())) + 1
    add_node.set_height(h1)
    return add_node

def get_right_most(root):
    while True:
        right_child = root.get_right()
        if right_child is None:
            break
        root = right_child
    return root.get_data()

def get_left_most(root):
    while True:
        left_child = root.get_left()
        if left_child is None:
            break
        root = left_child
    return root.get_data()

def del_node(root, data):
    left_child = root.get_left()
    right_child = root.get_right()
    if root.get_data() == data:
        if left_child is not None and right_child is not None:
            temp_data = get_left_most(right_child)
            root.set_data(temp_data)
            root.set_right(del_node(right_child, temp_data))
        elif left_child is not None:
            root = left_child
        elif right_child is not None:
            root = right_child
        else:
            return None
    elif root.get_data() > data:
        if left_child is None:
            print("No such data")
            return root
        else:
            root.set_left(del_node(left_child, data))
    else: # root.get_data() < data
        if right_child is None:
            return root
        else:
            root.set_right(del_node(right_child, data))

    if get_height(right_child) - get_height(left_child) == 2:
        if get_height(right_child.get_right()) > get_height(right_child.get_left()):
            root = left_rotation(root)
        else:
            root =right_left_rotation(root)
    elif get_height(right_child) - get_height(left_child) == -2:
        if get_height(left_child.get_left()) > get_height(left_child.get_right()):
            root = right_rotation(root)
        else:
            root = left_right_rotation(root)
    height = max_between(get_height(root.get_right()), get_height(root.get_left())) + 1
    root.set_height(height)
    return root


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self):
        return get_height(self.root)

    def insert(self, data):
        print("insert:" + str(data))
        self.root = insert_node(self.root, data)

    def del_node(self, data):
        print("delete:" + str(data))
        if self.root is None:
            print("Treee is empty!")
            return
        self.root = del_node(self.root, data)

    def __str__(self):
        output = ""
        q = my_queue()
        q.push(self.root)
        layer = self.get_height()
        if layer == 0:
            return output
        count = 0
        while not q.is_empty():
            node = q.pop()
            space = " " * int(math.pow(2, layer - 1))
            output += space
            if node is None:
                output += "*"
                q.push(None)
                q.push(None)
            else:
                output += str(node.get_data())
                q.push(node.get_left())
                q.push(node.get_right())
            output += space
            count += 1
            for i in range(100):
                if count == math.pow(2, i) - 1:
                    layer = layer - 1
                    if layer == 0:
                        output += "\n***************************"
                        return output
                    output += "\n"
                    break
        output += "\n***************************"
        return output


def _test():
    import doctest
    doctest.testmod();

if __name__ == "__main__":
    _test()
    t = AVLTree()
    lst = list(range(10))
    random.shuffle(lst)
    for i in lst:
        t.insert(i)
        print(str(t))
    random.shuffle(lst)
    for i in lst:
        t.del_node(i)
        print(str(t))
