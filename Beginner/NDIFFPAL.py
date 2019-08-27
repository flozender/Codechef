for _t in range(int(input())):
    s = 'abc'
    n = int(input())
    extra = n%3
    st = s*(n//3) + s[0:extra]
    print(st)
