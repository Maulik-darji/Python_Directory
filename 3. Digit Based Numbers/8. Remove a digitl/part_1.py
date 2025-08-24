r = int(input("Enter Range: "))
mylist = []
for i in range(r):
    ele = int(input(f"Enter Number {i+1}: "))
    mylist.append(ele)
print("List: ", mylist)

r_num = int(input("Enter Number to Remove: "))

if r_num in mylist:
    mylist.remove(r_num)
    print("Updated List: ", mylist)
else:
    pass

