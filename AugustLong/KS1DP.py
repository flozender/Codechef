def gen(start, end):
    
    if start > end:
        return 0

    if countdic[start][end] != None:
        return countdic[start][end]
    
    if end-1 == start:
        result = aList[start] ^ aList[end]
        countdic[start][end] = result
        return result

    else:
        result = gen(start, end-1) ^ aList[end]
        countdic[start][end] = result
        return result

for _t in range(int(input())):
    n = int(input())
    aList = list(map(int, input().split()))
    count = 0
    countdic = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        gen(i, n-1)

    for i in range(0,n):
        for j in range(i+1, n):
            val1 = countdic[i][j]
            # for k in range(i, j+1):
            #     val1 ^= aList[k]
            if val1 == 0:
                count += j+1-i-1

    print(count)