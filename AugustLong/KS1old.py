def prep(aList, n, countdic):
    for i in range(32):
        countdic[i][0] = 0
        for j in range(n):
            if j>0:
                countdic[i][j] = countdic[i][j-1]
            if aList[j] & (1 << i):
                countdic[i][j] += 1

def findx(start, end, countdic):
    val = 0
    for i in range(32):
        if end>0:
            sub = countdic[i][start-1]
        else:
            sub = 0

        num = countdic[i][end] - sub
        if num & 1:
            val += (1 << i)
    return val


for _t in range(int(input())):
    n = int(input())
    aList = list(map(int, input().split()))
    count = 0
    countdic = [[None for _ in range(n)] for _ in range(32)]
    
    prep(aList, n, countdic)

    print(findx(0, n-1, countdic))
    # print(countdic)

    # for i in range(0,n):
    #     for j in range(i+1, n):
    #         val1 = countdic[i][j]
    #         if val1 == 0:
    #             count += j+1-i-1

    # print(count)