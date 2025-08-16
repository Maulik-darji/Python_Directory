n = int(input("Enter Range: "))

for i in range(1,n+1):
    for j in range(i):
        print(j+1, end=" ")
    print()