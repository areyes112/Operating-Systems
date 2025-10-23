from heapq import heapify, heappush, heappop   

class StackMath:
    def __init__(self,val_a,val_b,val_c):
        self.val_a = val_a
        self.val_b = val_b
        self.val_c = val_c

    def func1(self):
        print("This is function 1 starting...")
        print("We will see function 2 complete before function 1 ends")
        self.func2()
        print("Function 1 ending now.")

    def func2(self):
        print("Function 2 starting...")
        print("We will see function 3 complete before function 2 ends")
        self.func3()
        print("Function 2 ending now.")

    def func3(self):
        print("This is function 3 starting...")
        print("Function 3 ending now.")
        return self.val_a + self.val_b + self.val_c
    
if __name__ == "__main__":

    heap1 = [1,2,3]
    heap2 = [4,5,6]
    StackMathInstance1 = StackMath(heap1)
    StackMathInstance2 = StackMath(heap2)
    StackMathInstance1.func1()
    StackMathInstance2.func1()
    
    