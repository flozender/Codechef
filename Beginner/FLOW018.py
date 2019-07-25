t = int(input())
num = []
def fact(n):
    if n == 1:
        return 1
    else: 
        return n*fact(n-1)
for i in range(t):
    num.append(int(input()))
for i in range(t):
    print (fact(num[i]))