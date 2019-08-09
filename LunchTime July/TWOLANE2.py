t = int(input())

for i in range(t):
    n, k, d = map(int, input().split())
    x_list = list(map(int, input().split()))
    l_list = list(map(int, input().split()))
    
    if(l_list[0] == 1):
        currLane = 2
        coor = 0
    else:
        currLane = 1
        coor = 0
    
    for x, lane in zip(x_list, l_list):
        if lane == currLane:
            pass
        else:
            coor = max(coor, x + 1)
#  Incomplete
    