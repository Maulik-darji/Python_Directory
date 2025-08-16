n = int(input("Enter Range for Fibonacci Series: "))

f_term = 0
s_term = 1

if n == 0:
    print("Enter Valid Range")
elif n == 1:
    print(f_term)
elif n == 2:
    print(f_term, s_term)
else:
    print(f_term, s_term, end=" ")
    for i in range(2, n-2):
        next = f_term + s_term
        f_term = s_term
        s_term = next
        print(next, end=" ")