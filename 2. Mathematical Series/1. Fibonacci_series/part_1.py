# Program to print Fibonacci series

# Ask the user for the number of terms
n = int(input("Enter the number of terms: "))

# First two terms
a, b = 0, 1

print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    # Update values
    a, b = b, a + b

