n = int(input())
a = [None]*n
b = [None]*n
for i in range(0, n):
    a[i],b[i] = map(int, input().split(' '))
for i in range(0, n):
    print(a[i]+b[i])