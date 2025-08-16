n = int(input("Enter Number To Find Factorial: "))
result = 1
temp = n
while temp > 0:
    result = result * temp
    temp = temp - 1
print(result)