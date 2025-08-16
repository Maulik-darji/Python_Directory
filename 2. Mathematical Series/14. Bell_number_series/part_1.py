import math

n = int(input("Enter Range for Bell Number: "))

bell = [0]*(n+1)

bell[0] = 1
for i in range(1, n+1):
    total = 0
    for k in range(i):
        total += math.comb(i-1, k)*bell[k]
    bell[i] = total
for i in range(n+1):
    print(f"Bell { i } = {bell[i]}")