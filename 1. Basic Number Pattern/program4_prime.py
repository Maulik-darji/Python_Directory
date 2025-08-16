arr=[]
class compositie():
    def compositie_num(self, c_range):
        self.c_range = c_range

        for i in range(4, c_range+1):
            for j in range(1, i+1):
                if i%j == 0:
                    arr.append(i)
            else:
                pass
        print(arr)
    
com = compositie()
user_range = int(input("Enter Range: "))
com.compositie_num(user_range)