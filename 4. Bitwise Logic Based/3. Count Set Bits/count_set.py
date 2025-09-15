# Kernighan's Algorithm is used to find the number of the set bits, Set bits are the binary number with the 1 

def count_set_bit(n):
    count = 0
    while n != 0:
        n = n & (n-1)
        count += 1
    return count

num = int(input("Enter Number: "))
print("Number of Set Bits: ", count_set_bit(num))

