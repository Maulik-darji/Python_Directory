ran_ge = int(input("Enter Range: "))
mylist = []
for i in range(ran_ge):
    mylist.append(i+1)
print(mylist)

num_choice = input("Enter Digit To Check Occurrence: ")  # keep as string
count = 0

for i in mylist:
    count += str(i).count(num_choice)   # counts all occurrences inside the number

print(f"{num_choice} occurs: {count} times")
