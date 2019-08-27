# prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
for _t in range(int(input())):
    p = int(input())
    ans = 0
    while p > 2048:
        p -= 2048
        ans += 1
    
    p = list(bin(p))
    ans += p.count('1')
    print(ans)