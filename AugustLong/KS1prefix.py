def xor(n):
    ex = [None for _ in range(n)]
    ex[0]=aList[0]
    for i in range(1,n):
        ex[i] = aList[i] ^ ex[i-1]
    count = 0
    seen = {}

    for i in range(n):
        try:
            seen[ex[i]] += 1
        except:
            seen[ex[i]] = 1

        if ex[i] == 0:
            count += i

    for i in range(n):
        for j in range(i+1,n):
            if ex[i] == ex[j]:
                count += j-i-1
###################################
    # for i in range(0,n):
    #     for j in range(i+1, n):
    #         if i != 0:
    #             val1 = ex[j] ^ ex[i-1]
    #         else:
    #             val1 = ex[j]
    #         print(val1)
    #         if val1 == 0:
    #             count += j-i
    #             print("at i & j", i, j)
    #             print("added", j-i)
    return count

for _t in range(int(input())):
    n = int(input())
    aList = list(map(int, input().split()))
    while 0 in aList:
        aList.remove(0)

    print(xor(len(aList)))