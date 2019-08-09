import math

def readVal(qFirst, qLast, first, last, node):
    # Total Overlap
    if qFirst <= first and qLast >= last:
        return s[node]
    # No Overlap
    elif last < qFirst or first > qLast:
        return 0

    mid = (first+last)//2

    return readVal(qFirst, qLast,first, mid, 2*node + 1) ^ readVal(qFirst, qLast, mid+1, last, 2*node + 2)


def genST(first, last, i):
    if first == last:
        s[i] = aList[first]
        return 
    mid = (first+last)//2
    genST(first, mid, (2*i)+1)
    genST(mid+1, last, (2*i)+2)
    s[i] = s[(2*i) + 1] ^ s[(2*i) + 2]
    return

for _t in range(int(input())):
    n = int(input())
    dups = 0
    aList = list(map(int, input().split()))
    if int(math.sqrt(n)+0.5)**2 == n:
        s = [0 for i in range(2*n+1)]
    else:
        sq = math.floor(math.sqrt(n)) + 1
        s = [0 for i in range(sq*sq*2+1)]
    for i in range(n):
        try:
            if i%2 == 0 and aList[i] == aList[i+1]:
                dups+=1
        except:
            pass
    
    genST(0, len(aList)-1, 0)
    
    vals = readVal(1, 3, 0, 5, 0)
    print(vals)
    print(s)
    print(2*s.count(0)-dups)