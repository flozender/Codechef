for _t in range(int(input())):
    n, k, d = map(int, input().split())
    xs = list(map(int, input().split()))
    ls = list(map(int, input().split()))
    my_x = 0
    my_l = 3 - ls[0]
    print("my_x",my_x)
    print("my_l",my_l)

    for x, l_ in zip(xs, ls):
        print("my_x = ", my_x)
        print("x = ",x,"l = ", l_)
        if l_ == my_l:
            print("caught")
            if x <= my_x:
                print("crashed")
                # crash
                print(x)
                break
            my_l = 3 - my_l
            print("new my_l", my_l)
            my_x = max(x + 1, my_x + d)
            print("new my_x", my_x)            
        else:
            my_x = max(x + 1, my_x)
    else:
        print(k)