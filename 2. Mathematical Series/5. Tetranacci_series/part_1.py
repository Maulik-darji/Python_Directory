n = int(input("Enter Range: "))

a,b,c,d = 0,0,1,1

print("Tetranacci Series: ")
for i in range(n):
    print(a, end=" ")
    a,b,c,d = b,c,d,a+b+c+d