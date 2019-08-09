d = {0:0, 1:1, 2:2, 3:3, 4:4}

def convert(n):
    if n in d:
        return d[n]
    else:
        d[n] = max(n, convert(n//4)+convert(n//3)+convert(n//2))
        return (d[n])


while True:
    try:
        n = int(input()) 
        print(convert(n))
    except:
        break