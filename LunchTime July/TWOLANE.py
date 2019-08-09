t = int(input())

x = [0 for i in range(t)]
l = [0 for i in range(t)]
# lane = [[0,0,0] for i in range(t)]


for i in range(t):
    lane = [0,0,0]
    n,k,d = map(int, input().split())
    x[i] = list(map(int, input().split()))
    l[i] = list(map(int, input().split()))
    lane[1] = [0 for i in range(k)]
    lane[2] = [0 for i in range(k)]
    for obs,lno in zip(x[i],l[i]):
        lane[lno][obs] = 'Blocked'  
    trav_dist = 0
    max = 0
    first = True
    if(lane[1].index('Blocked') >= lane[2].index('Blocked')):
        current = lane[1]
        other = lane[2]    
    elif (lane[1].index('Blocked') <= lane[2].index('Blocked')):
        current = lane[2]
        other = lane[1]
    for z in range(0,k):
        if current[z] != 'Blocked':
            trav_dist += 1
        elif current[z] == 'Blocked':
            if other[z-1] == 'Blocked':
                max = trav_dist
                break
            elif (first or trav_dist >= d): 
                first = False
                trav_dist += 1   
                current, other = other, current
            elif (trav_dist <= d):
                if max < trav_dist:
                    max = trav_dist
                break
    if max == 0:
        max = trav_dist
    print(max)