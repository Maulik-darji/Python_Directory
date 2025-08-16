n = int(input("Enter Number to Find Factorial: "))

temp = n
sum = 1
for i in range(n):
    sum = sum*temp
    temp = temp-1

print(sum)