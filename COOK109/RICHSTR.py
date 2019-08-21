for _t in range(int(input())):
    n , q = list(map(int, input().split()))
    s = input()
    for _q in range(q):
        l , r = list(map(int, input().split()))
        rich = False
        if r-l >= 3:
            right = l+3
            yes = "NO"

            while right <= r:
                dict = {}
                for i in range(l-1,right):
                    try:
                        dict[s[i]] += 1
                    except:
                        dict[s[i]] = 1
                for i,j in dict.items():
                    if j > (right-l-1)/2:
                        yes = "YES"
                        break
                right += 1
            print(yes)
        else:
            print("NO")
