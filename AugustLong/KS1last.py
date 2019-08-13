for _t in range(int(input())):
    n = int(input())
    aList = list(map(int, input().split()))
    count = 0
    for i in range(n):
        s = 0
        for j in range(i,n):
            s ^= aList[j]
            if s == 0:
                count += j-i
    print(count)
