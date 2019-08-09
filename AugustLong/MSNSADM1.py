for _t in range(int(input())):
    _ = input()
    goals = list(map(int, input().split()))
    fouls = list(map(int, input().split()))
    maxVal = 0
    for i,j in zip(goals, fouls):
        points = (i*20)-(j*10)
        if points >= maxVal:
            maxVal = points
    print(maxVal)
