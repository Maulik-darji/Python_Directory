n = int(input("Enter Range: "))
a, b = 0, 1

print("Fibonacci Series")
for i in range(n):
    print(a, end= " ")
    a, b = b, a+b