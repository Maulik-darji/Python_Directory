# Program to print Fibonacci series (beginner level)

# Ask the user how many numbers to print
n = int(input("Enter how many Fibonacci numbers you want: "))

# Start with first two numbers
first = 0
second = 1
if n == 0:
    print(" ")
elif n == 1:
    print(first)
elif n == 2:
    print(first, second)

else:
    print(first, second, end=" ")

    # Use a loop to calculate the rest
    for i in range(2, n):
        next_number = first + second
        print(next_number, end=" ")
        
        first = second
        second = next_number
