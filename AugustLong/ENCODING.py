def findfx(n):
    s = 0
    l = len(n)
    prev = None
    if len(set(n)) == len(n):
        return int("".join(n))
    for i in range(n):
        if n[i] == prev:
            n[i] = '0'
        else:
            prev = n[i]
            # s += n[i] * (10 ** (l-i-1))
    return int("".join(n))

for _t in range(int(input())):
    _, l = [int(x) for x in input().split()]
    _, r = [int(x) for x in input().split()]
    s = 0
    mod = 1000000007

    diff = r - l
    print(diff, "Diff")
    for i in range(l, r+1):
        print(findfx(list(str(i))))
        s = (s%mod+findfx(list(str(i)))%mod)%mod
        
    # print(findfx(list(str(12293284222)),len(str(12293294222-12293284222))))