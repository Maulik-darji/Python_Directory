f_range = int(input("Enter Range: "))

first = 0
second = 1

if f_range == 0:
    print("No num to display")
elif f_range == 1:
    print(first)

else:
    print(first, second, end=" ")
    for i in range(2, f_range):
        next_num = first+second
        print(next_num, end=" ")
        first = second 
        second = next_num