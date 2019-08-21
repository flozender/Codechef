for _t in range(int(input())):
    n , q = list(map(int, input().split()))
    p = list(map(int, input().split()))
    for _q in range(q):
        x = int(input())
        count = 0
        for i in range(n):
            if x > p[i]:
                print("i",i)

                count += 1
                x = 2*(x-p[i])
            else:
                break
        print("count",count)