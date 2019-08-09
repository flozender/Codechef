def bitwise(n1,n2):
    check = str(n1)+str(n2)
    if check in oper:
        return oper[check]
    elif n1+1 == n2 or n1 == n2:
        result = n1^n2
        oper[check] = result
        return result
    else:
        result = bitwise(n1,n2-1) ^ n2
        oper[check] = result
        return result

for _t in range(int(input())):
    n = int(input())
    aList = list(map(int, input().split()))
    oper = {}
    count = 0
    for i in range(n):
        for k in range(n, i, -1):
            for j in range(i+1,k):
                if bitwise(i,j-1) == bitwise(j, k):
                    count += 1
    print (count)
