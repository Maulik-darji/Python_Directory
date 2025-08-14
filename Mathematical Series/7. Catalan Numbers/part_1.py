import math 
r_range = int(input("Enter Range: "))
arr = []

for n in range(r_range):
    catalan = math.factorial(2*n)// (math.factorial(n)*math.factorial(n+1))
    arr.append(catalan)

print(arr)