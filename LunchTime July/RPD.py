t = int(input())
queries = [0 for i in range(t)]

for i in range(t):
    n = int(input())
    queries[i] = list(map(int, input().split()))

for query in queries:
    max = 0
    for i in range(0, len(query)):
        for j in range(1, len(query)):
            if(i != j):
                if sum(map(int, str(query[i]*query[j]))) > max:
                    max = sum(map(int, str(query[i]*query[j])))
    print(max)
