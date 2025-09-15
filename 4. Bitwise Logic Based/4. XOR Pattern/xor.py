#Swapping Numbers using the Xor
def swap_xor(a,b):
    print(f"Before Swapping a: {a}, b: {b}")
    a = a^b
    b = a^b
    a = a^b
    print(f"After Swapping a: {a}, b: {b}")
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))

swap_xor(num1, num2)

