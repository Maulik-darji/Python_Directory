n = int(input("Enter Original Number: "))
temp = n
rev = 0

while n > 0:
    next = n%10
    rev = rev*10 + next
    n = n // 10

print("Palindrome") if rev == temp else print("Not Palindrome")