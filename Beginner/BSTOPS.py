class Node:
    def __init__(self, value):
        self.value = value
    def addPos(self, pos):
        self.pos = pos
    def addLeft(self, left):
        self.left = left
    def addRight(self, right):
        self.right = right

q = int(input())
operations = [0 for i in range(q)]
queries = [0 for i in range(q)]

for i in range(q):
    operations[i], queries[i] = input().split()
queries = list(map(int, queries))

for i, j in zip(operations, queries):
    if i == 'i':
        nval = Node(j)
        
