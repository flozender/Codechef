x = input().split(" ")
a = int(x[0])
b = float(x[1])
if (a%5==0):
    if (a<=b+0.50 and b-a-0.50>0):
        z=(b-a-0.50)
        print("%.2f" % float(round(z,2)))
    else:
        print(b)
else:
    print(b)
