n = int(input("How Many Tribonacci to Print: "))

first = 0
second = 0
third = 1

if n == 1:
    print(first)
elif n == 2:
    print(first, second)
elif n == 3:
    print(first, second, third)
else:
    print(first, second, third, end=" ")
    for i in range(3, n):
        next = first + second + third
        print(next, end=" ")
        first, second, third = second, third, next