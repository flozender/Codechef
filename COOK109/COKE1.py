import math

for _t in range(int(input())):
    n, m, k, l, r = list(map(int, input().split()))
    c = [None for _ in range(n)]
    p = [None for _ in range(n)]
    sat = [False for _ in range(n)]
    for i in range(n):
        c[i], p[i] = list(map(int, input().split()))

        if c[i] > k and m >= c[i]-k:
            sat[i] = True
        elif c[i] < k and m >= k-c[i]:
            sat[i] = True
        elif c[i] == k and m == 0:
            sat[i] = True
    print(sat)
    mi = math.inf
    for i in range(n):
        if sat[i]:
            if mi > p[i]:
                mi = p[i]
    if mi == math.inf:
        print(-1)
    else:
        print(mi) 
    