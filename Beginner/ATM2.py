t = int(input())
n = [0 for i in range(t)]
k = [0 for i in range(t)]
a = [[0] for i in range(t)]

for i in range(t):
    n[i],k[i] = map(int, input().split())
    a[i] = list(map(int, input().split()))

for i in range(t):
    result = ""
    for amount in a[i]:
        if amount <= k[i]:
            k[i] -= amount
            result += "1"
        else:
            result += "0"
    print(result)