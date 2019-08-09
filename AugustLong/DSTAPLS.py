for _t in range(int(input())):
    n,k = list(map(int, input().split()))
    print("NO") if (n//k)%k == 0 else print("YES")
