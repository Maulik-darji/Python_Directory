def set_bit(num, pos):
    return num | (1 << pos)
def unset_bit(num, pos):
    return num & ~(1<<pos)
def toggle_bit(num , pos):
    return num ^ (1<< pos)

if __name__ == "__main__":
    num = int(input("Enter Integer Number: "))
    pos = int(input("Enter bit position (0 for LSB)"))
    print("Original ", )
    print(f"Decimal: {num}, Binary:{bin(num)}")