
f_term = int(input("Enter 1st Term: "))
C_diff = int(input("Enter Common Difference: "))
r_series = int(input("Enter Range: "))
arr = [f_term]  
series = f_term
for i in range(1, r_series):
    series = series + C_diff
    arr.append(series)
print(arr)
print("n-th term: ",series)
nth_choice = int(input("Want to Find n-th Term\n1. Yes\n2. No\n"))
if nth_choice == 1:
    nth_num = int(input("Enter nth Term: "))
    nth_formula = f_term + (nth_num-1)*C_diff
    print("nth term is: ",nth_formula)
