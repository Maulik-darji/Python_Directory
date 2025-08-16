def factorial(num):
    return 1 if num == 0 else num * factorial(num - 1)

n = int(input("Enter Number To Find factorial: "))
print(factorial(n))