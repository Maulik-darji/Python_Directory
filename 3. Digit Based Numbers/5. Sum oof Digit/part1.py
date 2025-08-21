n = int(input("Enter List Size: "))
mylist = []
sum = 0
for i in range(n):
    ele = int(input(f"Enter Number {i+1}: "))
    mylist.append(ele)
    sum = sum + ele
print("List: ", mylist)
print("Sum: ", sum)
