t = int(input())
ans = [0 for i in range(t)]
for i in range(t):
    ans[i] = int(input())
for i in sorted(ans):
    print(i)