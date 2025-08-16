r = int(input("Enter Range: "))

cube_sum = 0
for i in range(1, r+1):
    formula = (i*i)*i
    cube_sum = formula
    print(cube_sum, end=" ")