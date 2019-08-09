t = int(input())
queries = [0 for i in range(t)]

for i in range(t):
    n, q = list(map(int, input().split()))
    for i in range(0,len(q)):
        queries[i] = list(map(int, input().split())) 