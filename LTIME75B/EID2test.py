ra = int(input())
cond = [None for _ in range(ra)]
for t in range(ra):
    a = [0,0,0]
    c = [0,0,0]
    a[0], a[1], a[2], c[0], c[1], c[2] = list(map(int, input().split()))
    cnew = [0,0,0]
    asorted = sorted(a)
    for i in range(3):
        m = min(a)
        mn = a.index(m)
        a[mn] = 99999999
        cnew[i] = c[mn]
    cond[t] = "FAIR"
    for i in range(3):
        try:
            if asorted[i] < asorted[i+1]:
                if cnew[i] >= cnew[i+1]:
                    cond[t] = "NOT FAIR"
                    break
            elif asorted[i] == asorted[i+1]:
                if cnew[i] != cnew[i+1]:
                    cond[t] = "NOT FAIR"
                    break
            elif asorted[i] == asorted[i+2]:
                if cnew[i] != cnew[i+2]:
                    cond[t] = "NOT FAIR"
                    break
        except:
            pass
        
for t in range(ra):
    print(cond[t])
        
# try:
#             if asorted[i] == asorted[i-1]:
#                 if cnew[i] != cnew[i-1]:
#                     cond[t] = "NOT FAIR"
#                     break
#             if asorted[i] == asorted[i-2]:
#                 if cnew[i] != cnew[i-2]:
#                     cond[t] = "NOT FAIR"
#                     break
#         except:
#             pass
#         try:
#             if cnew[i] > cnew[i+1]:
#                 cond[t] = "NOT FAIR"
#                 break
#         except:
#             pass