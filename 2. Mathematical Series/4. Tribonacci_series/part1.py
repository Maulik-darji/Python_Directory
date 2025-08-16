n = int(input("Enter Range: "))

a, b, c = 0, 0, 1

print("Tribonacci Series: ")
for i in range(n):
    print(a, end=" ")
    a,b,c = b,c,a+b+c   