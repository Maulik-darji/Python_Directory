n = int(input("Enter Number: "))

o_choice = int(input("\n\tOperations\n\t1. Convert to Binary\n\t2. Convert to Octal\n\t3. Convert to Hexadecimal\nEnter your Choice: "))

holder = ""

if o_choice == 1:
    temp = n
    while temp > 0:
        remain = temp % 2
        holder = str(remain) + holder
    print("Binary: ", holder)

elif o_choice == 2:
    hex_digits = "0123456789ABCDEF"
    temp = n

    while temp > 0:
        remain = temp%16
        holder = hex_digits[remain] + holder
        temp //= 16
    print("Hexadecimal: ", holder if holder else "0")

elif o_choice == 3:
    temp = n
    while temp > 0:
        remain = temp % 8
        holder = str(remain)+ holder
        temp //= 8
    print("Octal: ", holder if holder else "0")

else:
    print("Invalid Choice")