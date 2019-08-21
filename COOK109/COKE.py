import math

for _t in range(int(input())):
    n, m, k, l, r = list(map(int, input().split()))
    c = [None for _ in range(n)]
    p = [None for _ in range(n)]
    sat = [False for _ in range(n)]
    for i in range(n):
        c[i], p[i] = list(map(int, input().split()))
    for i in range(n):
        mini = m
        start = True
        while c[i] != k and mini > 0:
            while c[i] > k and mini>0:
                mini -= 1
                c[i] -= 1
            while c[i] < k and mini>0:
                mini -= 1
                c[i] += 1
    
        if l <= c[i] and c[i] <= r:
            sat[i] = True
    mi = math.inf
    for i in range(n):
        if sat[i]:
            if mi > p[i]:
                mi = p[i]
    if mi == math.inf:
        print(-1)
    else:
        print(mi) 
    