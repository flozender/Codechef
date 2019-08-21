cipher = input()
k1 = int(input())
k2 = int(input())
key = {
   "A": 0,
   "B": 1,
   "C": 2,
   "D": 3,
   "E": 4,
   "F": 5,
   "G": 6,
   "H": 7,
   "I": 8,
   "J": 9,
   "K": 10,
   "L": 11,
   "M": 12,
   "N": 13,
   "O": 14,
   "P": 15,
   "Q": 16,
   "R": 17,
   "S": 18,
   "T": 19,
   "U": 20,
   "V": 21,
   "W": 22,
   "X": 23,
   "Y": 24,
   "Z": 25
}
key2 = {
   0: "A",
   1 :"B",
   2 :"C",
   3 :"D",
   4 :"E",
   5 :"F",
   6 :"G",
   7 :"H",
   8 :"I",
   9 :"J",
   10 :"K",
   11 :"L",
   12: "M",
   13: "N",
   14: "O",
   15: "P",
   16: "Q",
   17: "R",
   18: "S",
   19: "T",
   20: "U",
   21: "V",
   22: "W",
   23: "X",
   24: "Y",
   25: "Z"
}

cipher = list(cipher)
n = len(cipher)


cipher_num = [0 for i in range(n)]

for i in range(n):
    cipher_num[i] = key[cipher[i]]
plain = [0 for i in range(n)]

# start = 1
# vals = [1]
# for i in range(1,27):
#     vals.append(vals[i-1]+26)
# print(vals)
j = 1
k2inv = 0
while 1:
    if (j*k2)%26 == 1:
        k2inv = j
        break
    j += 26

for i in range(n):
    plain[i] = ((cipher_num[i] - k1) * k2inv)%26
plain_ans = []

for i in plain:
    plain_ans.append(key2[i])
print("".join(plain_ans))