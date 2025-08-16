import math
n = int(input("Enter Range to print Pascals triangle: "))

for i in range(n):
    print(" "*(n-i), end="")
    for j in range(i+1):
        print(math.comb(i,j), end=" ")
    print()