def genMat(arr, res, n):
    for i in range(n):
        for j in range(n):
            res[i][j] = arr[i] ^ arr[j]
    return res


for _t in range(int(input())):
    n = int(input())
    aList = list(map(int, input().split()))
    res = [[0 for _ in range(n)] for _ in range(n)]

    res = genMat(aList, res, n)
    