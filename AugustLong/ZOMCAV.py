def prefsum(arr):
    for i in range(1,len(arr)):
        arr[i] = arr[i]+arr[i-1]
    arr.pop()
    del arr[0]
    return arr
for _t in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    h = list(map(int, input().split()))
    radLevel = [0 for i in range(n+2)]
    lm = len(radLevel)
    for i in range(0,n):
        radLevel[max(1,i+1-c[i])] += 1
        radLevel[min(i+1+c[i]+1, n+1)] -= 1

    radLevel = prefsum(radLevel)
    if sorted(h) == sorted(radLevel):
        print("YES")
    else:
        print("NO")

