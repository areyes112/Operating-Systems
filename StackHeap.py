class StackMath:
    def __init__(self,val_a,val_b,val_c):
        self.val_a = val_a
        self.val_b = val_b
        self.val_c = val_c

    def funcA(self):
        print("==========Function 1 Starting==========\n")
        self.funcB()
        print("==========Function 1 Ending==========\n")

    def funcB(self):
        print("----------Function 2 Starting----------\n")
        self.funcC()
        print("----------Function 2 Ending----------\n")

    def funcC(self):
        print("###########Function 3 Starting###########\n")
        print(f"Values are: {self.val_a}, {self.val_b}, {self.val_c}\n")
        print("###########Function 3 Ending###########\n")

    
if __name__ == "__main__":

    heap1 = [1,2,3]

    StackMathInstance1 = StackMath(*heap1)

    StackMathInstance1.funcA()

    
    