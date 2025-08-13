# input = range
# input = odd or Odd_even

class Odd_even:
    def odd(self, print_range, choice):
        self.print_range = print_range
        self.choice = choice
        if choice == 1:
            for i in range(print_range):
                    if i%2==0:
                        print(i, end=", ")
                    else:
                        pass
        elif choice == 2:
            for i in range(print_range):
                    if i%2 != 0:
                        print(i, end=", ")
                    else: 
                        pass
odd_even = Odd_even()
user_range = int(input("Enter Range: "))
user_choice = int(input("1.) Even\n2.) Odd"))
odd_even.odd(user_range,user_choice)

