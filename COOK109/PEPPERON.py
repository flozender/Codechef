for _t in range(int(input())):
    n = int(input())
    pizza = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        pizza[i] = list(map(int,list(input())))
    mid = n//2
    h1 = 0
    h2 = 0
    half1 = [None for _ in range(n)]
    half2 = [None for _ in range(n)]

    for i in range(n):
        half1[i] = pizza[i][0:mid].count(1)
        half2[i] = pizza[i][mid:n].count(1)
        h1 += half1[i]
        h2 += half2[i]
    
    if h2-h1 == 0:
        print(0)
    else:
        leastdiff = abs(h2-h1)
        for i in range(n):
            if abs(h2-h1)>0:
                half1[i], half2[i] = half2[i], half1[i]
                h2, h1 = sum(half2), sum(half1)
                half1[i], half2[i] = half2[i], half1[i]
            if abs(h2-h1) < leastdiff:
                leastdiff = abs(h2-h1)
        print(leastdiff)          