size = int(input("Enter AP Series Range: "))
arr = []
for i in range(size):
    ele = int(input(f"Enter Element {i+1}: "))
    arr.append(ele)

c_diff = arr[1] - arr[0]

print("AP Series: ",arr)
op = int(input("AP Series Operations\n\t1.) Find Sum\n\t2.) Find Common Difference\n\t3.) Find nth Term: \nEnter Your Input: "))

n_pass = 0
n_term = 0
n_sum = sum(arr) 
# fix = fix with directly using the sum(arr)

if op == 1:
    print("Sum: ",n_sum)

elif op == 2:
    is_ap = True
    for i in range(size-1):
        # error fix with size-1 and not 1, size
        if  arr[i+1] - arr[i] != c_diff:
            is_ap = False
            break
    if is_ap:
        print("Common Difference: ",c_diff)
    else:
        print("Invalid Series")
