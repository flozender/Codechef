t = int(input())
a = [[0 for x in range(12)] for y in range(t)]
for i in range(0, t):
    d = {}
    for j in range(0, 12):
        z = input().split(' ')
        a[i][j] = z
        a[i][j][1] = int(a[i][j][1])
        a[i][j][3] = int(a[i][j][3])

        if (a[i][j][0] not in d):
            d[a[i][j][0]] = {"points": 0, "gd": 0}


        if (a[i][j][4] not in d):
            d[a[i][j][4]] = {"points": 0, "gd": 0}

        if (a[i][j][1] > a[i][j][3]):
            d[a[i][j][0]]["points"] += 3

        elif(a[i][j][1] < a[i][j][3]):
            d[a[i][j][4]]["points"] += 3

        else:
            d[a[i][j][0]]["points"] += 1
            d[a[i][j][4]]["points"] += 1

        d[a[i][j][0]]["gd"] += a[i][j][1]-a[i][j][3]
        d[a[i][j][4]]["gd"] += a[i][j][3]-a[i][j][1]
        # print(d)

    max = 0
    it = None
    ans = []
    gd = None
    for x,y in d.items():
        if y["points"] > max:
            max = y["points"]
            it = x
            gd = y["gd"]

        elif y["points"] == max and y["points"] != 0:
            if y["gd"] > gd:
                it = x

        elif y["points"] == 0 and it == None:
            it = x

    ans.append(it)
    d.pop(it)

    max = 0
    for x,y in d.items():
        if y["points"] > max:
            max = y["points"]
            it = x
            gd = y["gd"]
            
        elif y["points"] == max and y["points"] != 0:
            if y["gd"] > gd:
                it = x

        elif y["points"] == 0 and it == None:
            it = x

    ans.append(it)
    print(ans[0], ans[1])