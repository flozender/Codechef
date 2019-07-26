t = int(input())
a = [0 for i in range(t)]
b = [0 for i in range(t)]

for i in range(t):
    a[i], b[i] = input().split()
a = list(map(int, a))
b = list(map(int, b))


for i,j in zip(a,b):

    while(i<j):
        j = j -1
    while(i>j):
        i = i -1
    if(i == j):
        print("YES")