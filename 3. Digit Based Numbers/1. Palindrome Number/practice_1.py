ori = int(input("Enter Number to Check Palindrome: "))

temp = ori
rev  = 0

while ori > 0:
    next = ori % 10
    rev = rev * 10 + next
    ori = ori // 10
if rev == temp:
    print("Palindrome")
else:
    print("Not Palindrome")