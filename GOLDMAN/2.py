import math
# def find_fac(x):
#         fact = []
#         for i in range(2, x):
#             if x % i == 0:
#                 prime = True
#                 for j in range(2,int(math.sqrt(i))):
#                     print(i,j)
#                     if i%j == 0:
#                         prime = False
#                 if prime:
#                     fact.append(i)
#         return fact

def isPrime(n):
    prime = True
    for i in range(2,n):
        if n%i == 0:
            prime = False
    return prime


def getSubsets(k, n, arr):
    # Write your code here
    pass
# print(find_fac(8))
print(isPrime(14))