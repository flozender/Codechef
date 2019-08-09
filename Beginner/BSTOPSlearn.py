class Node:
    def __init__(self, data, pos):
        self.data = data
        self.left = None
        self.right = None
        self.pos = pos

def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.data, p)
        inOrder(root.right)

def min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def insert(node, data, pos):
    if node is None:
        print(pos)
        return Node(data, pos)
    elif data<node.data:
        node.left = insert(node.left, data, pos*2)
    elif data>node.data:
        node.right = insert(node.right, data, 2*pos+1)
    return node

def remove(root, data):
    if root is None:
        return root
    if data<root.data:
        root.left = remove(root.left, data)
    elif data>root.data:
        root.right = remove(root.right, data)
    else:
        print(root.pos)
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = min_value(root.right)
        root.data = temp.data
        root.right = remove(root.right, temp.data)
    return root

root = None
queries = int(input())
for q in range(queries):
    query = [x for x in input().split()]
    if query[0]=="i":
        root = insert(root, int(query[-1]), 1)
    else:
        root = remove(root, int(query[-1]))
