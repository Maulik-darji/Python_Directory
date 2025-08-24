num = int(input("Enter Number: "))

operations = int(input("\t*** OPERATIONS ***\n\t1. Convert to Binary\n\t2. Convert to Hex\n\t3. Convert to Octal\nEnter Your Choice: "))
holder = ""
if operations == 1:  # Binary
    
    temp = num
    while temp > 0:
        remain = temp % 2
        holder = str(remain) + holder   # add remainder to front
        temp //= 2
    print("Binary:", holder)

elif operations == 2:
    hex_digits = "0123456789ABCDEF"
    temp = num

    while temp > 0:
        remain = temp%16
        holder = hex_digits[remain] + holder
        temp //= 16
    print("Hexadecimal: ", holder if holder else "0")

elif operations == 3:
    temp = num
    while temp > 0:
        remain = temp % 8
        holder = str(remain) + holder
        temp //= 8
    print("Octal: ", holder if holder else "0")

else:
    print("Invalid Choice")