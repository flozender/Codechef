q = int(input())
operations = [0 for i in range(q)]
queries = [0 for i in range(q)]

class Node:
    

for i in range(q):
    operations[i], queries[i] = input().split()
queries = list(map(int, queries))

for i, j in zip(operations, queries):
    if i == 'i':
