n = int(input("Enter Number to Reverse: "))

temp = n
rev = 0

while n > 0:
    next = n % 10
    rev = rev * 10 + next
    n = n // 10
print("Rev: ", rev)