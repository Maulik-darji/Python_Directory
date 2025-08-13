arr =[]
class prime():
    def prime_fun(self, cl_range):
        self.cl_range = cl_range
        for i in range(2, cl_range+1):
            for j in range(2, i):
                if i%j == 0:
                    break
            else:
                arr.append(i)
        print(arr)
print_prime = prime()
user_range = int(input("Enter Range: "))
print_prime.prime_fun(user_range)