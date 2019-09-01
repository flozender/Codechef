for _t in range(int(input())):
    a = [0,0,0]
    c = [0,0,0]
    a[0], a[1], a[2], c[0], c[1], c[2] = list(map(int, input().split()))
    
    cont = True
    cond = "FAIR"    
    # if a[0] == a[1] == a[2]:
    #     if c[0] == c[1] == c[2]:
    #         print("FAIR")
    #         cont = False
    #     else:
    #         print("NOT FAIR")
    #         cont = False
    if cont:
        for i in range(3):
            print(a, c)
            age = max(a)
            cash = max(c)
            if a.index(age) != c.index(cash):
                cond = "NOT FAIR"
            a.remove(age)
            c.remove(cash)
        print(cond)
