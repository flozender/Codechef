def flip(n):
    if n > 0:
        try:
            s[n-1] = 1-s[n-1]
        except:
            pass
    try:
        s[n+1] = 1-s[n+1]
    except:
        pass
    s[n] = None
    
for _t in range(int(input())):
    sIn = str(input())
    s = list(map(int,list(sIn)))
    lose = s.count(1)%2 == 0
    while 1 in s and not lose:
        try:
            if s[i] == None and s[i+1] == 0 and s[i+2] == None:
                break
        except:
            pass
        for i in range(s.index(1),len(s)):
            if s[i] == 1:
                flip(i)
    if lose or 0 in s:
        print("LOSE")
    else:
        print("WIN")

    # print("LOSE") if 0 in s else print("WIN")
