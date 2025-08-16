import math

n = int(input("Enter Number: "))
temp = n
sum = 0
n_convert = str(n)
n_len = len(n_convert)
while n > 0:
    next = n%10
    n = n// 10
    sum = sum + int(math.pow(next, n_len))

if sum == temp:
    print("Arm")
else:
    print("not")