    for i in range(1, n+1):
        print(" " * (n - i), end="")  # leading spaces
        print("# " * i)               # numbers with a space

    # Bottom inverted pyramid
    for i in range(n-1, 0, -1):      # start from n-1 down to 1
        print(" " * (n - i), end="")  # leading spaces
        print("# " * i)               # numbers with a space
