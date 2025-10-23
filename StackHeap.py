class StackMath:
    def __init__(self,val_a,val_b,val_c):
        self.val_a = val_a
        self.val_b = val_b
        self.val_c = val_c

    def funcA(self):
        print("==========Function 1 Starting==========")
        self.funcB()
        print("==========Function 1 Ending==========")

    def funcB(self):
        print("----Function 2 Starting----")
        self.funcC()
        print("----Function 2 Ending----")

    def funcC(self):
        print("****Function 3 Starting****")
        print(f"Values are: {self.val_a}, {self.val_b}, {self.val_c}")
        print("****Function 3 Ending****")

    
if __name__ == "__main__":

    heap1 = [1,2,3]
    heap2 = [4,5,6]

    StackMathInstance1 = StackMath(*heap1)
    StackMathInstance2 = StackMath(*heap2)
    StackMathInstance1.funcA()
    StackMathInstance2.funcA()
    
    