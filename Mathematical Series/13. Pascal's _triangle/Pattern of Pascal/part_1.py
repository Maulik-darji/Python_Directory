n = int(input("Enter Range: "))

for i in range(1, n+1):
    # Print leading spaces
    print(" " * (n - i), end="")
    
    # Print numbers from 0 to i-1
    for j in range(i):
        print(j, end=" ")
    
    # Move to next line
    print()
