choice = int(input("\n\t1. Print Arithmetic Series\n\t2. Operation on AP\n"))

if choice == 1:
    s_range = int(input("Enter Size of AP: "))
    f_term = int(input("Enter Term 1: "))
    c_diff = int(input("Enter Common Difference: "))
    next = f_term
    arr = [next]
    for i in range(1, s_range):
        next = next+c_diff
        arr.append(next)
    print("Your Series: ", arr)
    next_choice = int(input("Want to Find Nth Term ?\n\t1. YES\n\t2. No\n"))
    if next_choice == 1:
        nth_index = int(input("Enter index: "))
        nth_term_formula = f_term + ((nth_index - 1)*c_diff)
        print("Nth Terms: ", nth_term_formula)

elif choice == 2:
        series_choice = int(input("\n\t1. Continue with the default Series ?\n\t2. Create New Series\n"))
        while True:
            if series_choice == 1:
                default_series = [1, 3, 5, 7, 9, 11, 13, 15]  # global value
                default_c_diff = default_series[1] - default_series[0]
                print("\n***** OPERATIONS *****")
                default_operations = int(input("\t1. Nth Term\n\t2. Sum of Nth Term\n\t3. Sum of Series\n\t4. Find Common difference\n\t5. Exit\n"))
                
                if default_operations == 1:
                    nth_default_index = int(input("Enter Index: "))
                    default_nth_formula = default_series[0] + ((nth_default_index - 1) * default_c_diff)
                    print("Nth Term: ", default_nth_formula)
                
                elif default_operations == 2:
                    nth_default_index = int(input("Enter N (number of terms to sum): "))
                    default_nth_formula = default_series[0] + ((nth_default_index - 1) * default_c_diff)
                    default_sum = (nth_default_index / 2) * (default_series[0] + default_nth_formula)
                    print("Sum of first", nth_default_index, "terms: ", default_sum)
                
                elif default_operations == 3:
                    default_series_sum = sum(default_series)
                    print("Sum of the Default Series: ", default_series_sum)
                
                elif default_operations == 4:
                    print("Common Difference: ", default_c_diff)
                
                elif default_operations == 5:
                    print("Exiting...")
                    break  # exit the while loop
                
                else:
                    print("Invalid choice. Try again.")

            elif series_choice == 2:
                create_choice_size = int(input("Enter Size: "))
                f_term = int(input("Enter Term 1: "))
                c_diff = int(input("Enter Common Difference: "))
                next = f_term
                arr = [next]
                for i in range(1, create_choice_size):
                    next = next+c_diff
                    arr.append(next)
                print("Your AP Series: ", arr)


