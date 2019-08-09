def a(n1, n2):
    if n1 in s:
        return s[n1]
    else:
        return n2

for i in range(2):
    n1 = int(input())
    n2 = int(input())
    s = {1: "ok"}
    print(a(n1,n2))
