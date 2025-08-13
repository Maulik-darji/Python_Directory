import math
r_range = int(input("Enter Range: "))
arr = [float(input(f"Enter Element{i+1}: ")) for i in range(r_range)]

Operation = int(input(
    "Choose Operation\n"
    "\t1: Check if Geometric Progression\n"
    "\t2: Find Sum\n"
    "\t3: Find Common Ratio\n"
    "\t4: nth Number: \n"
))

if Operation == 1:
    if r_range < 2:
        print("Not Enough Number of Terms")
    else:
        try:
            c_ratio = arr[1]/arr[0]
            tolerance = 1e-9
            is_geo = all(math.isclose(arr[j]/ arr[j-1], c_ratio, rel_tol=tolerance) for j in range(1, r_range))
            if is_geo:
                print(f"It's Geometric, with common ratio: {c_ratio}")
            else:
                print("It's not Geometric sequence")
        except ZeroDivisionError:
            print("Sequence Containse zero - Cannot check ratio")