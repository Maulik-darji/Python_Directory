import math

n = int(input("Enter Bell Number Range: "))

# store Bell numbers
bell = [0] * (n+1)
bell[0] = 1   # base case

# recurrence
for i in range(1, n+1):
    total = 0
    for k in range(i):
        total += math.comb(i-1, k) * bell[k]
    bell[i] = total

# print results
for i in range(n+1):
    print(f"B{i} = {bell[i]}")

