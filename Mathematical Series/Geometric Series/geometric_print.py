r_geo = int(input("Enter the Range: "))
initial = int(input("Enter Initial Number: "))
ratio = int(input("Enter the Common Ratio: "))
arr = []
for i in range(r_geo):
    arr.append(initial)
    initial = initial*ratio
print("Geometric Series: ", arr)