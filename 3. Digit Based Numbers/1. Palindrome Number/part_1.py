# palindrome number is number whose reverse is same as the original number

ori = int(input("Input Original Number: "))
temp = ori        # keep a copy of the original number
rev = 0

while ori > 0:
    next = ori % 10
    rev = rev * 10 + next
    ori = ori // 10

if rev == temp:
    print("Palindrome")
else:
    print("Not Palindrome")
