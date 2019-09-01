for _t in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    minus = a.count(-1)
    if minus > n//2 or minus == 0:
        print("YES")
        for i in a:
            print(i, end = " ")
    else:
        print("NO")