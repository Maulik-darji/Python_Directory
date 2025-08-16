r = int(input("Enter Range for Lucas Series: "))
f_term = 2
s_term = 1

if r == 1:
    print(f_term)
elif r == 2:
    print(f_term, s_term)
else:
    print(f_term, s_term, end=" ")
    for i in range(r-2):
        next = f_term + s_term
        f_term = s_term
        s_term = next
        print(next, end=" ")
