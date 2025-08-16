import math

r = int(input("Enter Bell Num Range: "))

bell = [0] * (r+1)

bell[0] = 1

for i in range(1, r+1):
    total_sub = 0
    for k in range(i):
        total_sub += math.comb(i-1, k)*bell[k]
    bell[i] = total_sub

for i in range(r+1):
    print(f"Bell{i} = {bell[i]}")

