for _t in range(int(input())):
    sIn = str(input())
    s = list(map(int,list(sIn)))
    lose = s.count(1)%2 == 0
    if lose:
        print("LOSE")
    else:
        print("WIN")
