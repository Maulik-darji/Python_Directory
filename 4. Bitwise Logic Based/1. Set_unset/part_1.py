def set_bit(num, pos):
    return num | (1 << pos)

def unset_bit(num, pos):
    return num & ~(1 << pos)

def toggle_bit(num, pos):
    return num ^ (1 << pos)


# Main Program
# if is used when you only want to use the function and don't want to output any other things below written
# hence in this program also the program can be exe normally without the if function    

if __name__ == "__main__": 
    # Taking input
    num = int(input("Enter an integer number: "))
    pos = int(input("Enter bit position (0 for LSB): "))

    print("\nOriginal Number:")
    print(f"Decimal: {num}, Binary: {bin(num)}")

    # Set bit
    num_set = set_bit(num, pos)
    print(f"\nAfter Setting bit {pos}:")
    print(f"Decimal: {num_set}, Binary: {bin(num_set)}")

    # Unset bit
    num_unset = unset_bit(num, pos)
    print(f"\nAfter Unsetting bit {pos}:")
    print(f"Decimal: {num_unset}, Binary: {bin(num_unset)}")

    # Toggle bit
    num_toggle = toggle_bit(num, pos)
    print(f"\nAfter Toggling bit {pos}:")
    print(f"Decimal: {num_toggle}, Binary: {bin(num_toggle)}")
