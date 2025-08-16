n = int(input("Enter Number to Check Armstrong: "))
temp = n 
sum = 0
n_len = len(str(n))

while n > 0:
    digit = n%10
    n = n // 10
    sum += digit ** n_len

print("Armstrong") if sum == temp else print("Not Armstrong") 