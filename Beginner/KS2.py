def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

for _t in range(int(input())):
    n = int(input())
    count, val, currentNo = 0,19, 0
    while True:
        if sum_digits(val)%10 == 0:
            current = val
            currentNo += 1
        if currentNo == n:
            break
        val += 1
    print(current)