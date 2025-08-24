r = int(input("Enter Range: "))

mylist = []

for i in range(r):
    mylist.append(i+1)
print("List: ", mylist)

num = (input("Enter Number to Find Occurance: "))
o = 0
for i in mylist:
    o += str(i).count(num)
print(o)