r = int(input("Enter Range to Print Triangular Number: "))

tri_sum = 0
for i in range(1, r+1):
    tri_sum += i
    print(tri_sum, end=" ")