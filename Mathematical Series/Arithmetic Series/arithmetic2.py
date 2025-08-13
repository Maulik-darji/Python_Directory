f_term = int(input("Enter Number: "))
c_diff = int(input("Enter Common Difference: "))
t_range = int(input("Enter Range: "))

arr = []
series = f_term
for i in range(1, t_range):
    arr.append(series)
    series = series + c_diff
print(arr)
