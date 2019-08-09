class Node:
    def __init__(self, val):
        self.val = val
    def addLeft(self, left):
        self.left = left
    def addRight(self, right):
        self.right = right


a = Node(12)
print (a.val)
b = Node(13)
a.left = b
