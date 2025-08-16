n = int(input("Enter Range for Pell Number: "))
f_term = 0
s_term = 1
if n == 0:
    print("No Number to print")
elif n == 1:
    print(f_term)
elif n == 2:
    print(f_term, s_term)
else:
    print(f_term, s_term, end=" ")
    for i in range(1, n-2):
        next = 2*(s_term)+f_term
        f_term = s_term
        s_term = next
        print(next, end=" ")