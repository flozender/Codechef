t = int(input())
queries = [0 for i in range(t)]

for i in range(t):
    n = int(input())
    queries[i] = list(map(int, input().split()))
for query in queries:
    max = 0
    for i in range(0, len(query)):
        for j in range(0, len(query)):
            query[i]
    for i,j in enumerate(query):
        print(i,j)
        max += i*j
    