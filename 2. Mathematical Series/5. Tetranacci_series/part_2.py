n = int(input("Print Tetranacci Series Till: "))

first = 0
second = 0
third = 1
fourth = 1

if n == 1:
    print(first)
elif n == 2:
    print(second)
elif n == 3:
    print(third)
elif n == 4:
    print(fourth)
else:
    print(first, second, third, fourth, end=" ")
    for i in range(n):
        next = first+second+third+fourth
        print(next, end=" ")
        first, second, third = second, third, next