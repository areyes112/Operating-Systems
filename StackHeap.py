class StackMath: # Demonstrates stack and heap behavior
    def __init__(self, val_a, val_b, val_c):
        self.val_a = val_a
        self.val_b = val_b
        self.val_c = val_c

        self.heap_ref = [val_a, val_b, val_c]

    def startFunc(self): # Initiates the stack demonstration
        print("\n=== Demonstrating Stack (FILO) Behavior ===\n")
        self.funcA()
        print("\n=== Stack Unwinding Complete ===\n")

        print("\n=== Demonstrating Heap (Memory Storage) Behavior ===\n")
        self.showHeap()

    def funcA(self): # First function in the call stack
        print("========== Function A  =======\ \n")
        self.funcB()
        print("========== Function A  =======/ \n")

    def funcB(self): # Second function in the call stack
        print("========== Function B  ========\ \n")
        self.funcC()
        print("========== Function B  ========/ \n")

    def funcC(self): # Third function in the call stack
        print("========== Function C  =========\ \n")
        print(f"Values in local scope: {self.val_a}, {self.val_b}, {self.val_c}  | \n")
        print("========== Function C  =========/ \n")

    def showHeap(self): # Demonstrates heap behavior
        print(f"Heap reference ID: {id(self.heap_ref)}") # This calls the memory address of the heap object
        print(f"Heap contents: {self.heap_ref}") #This shows the contents of the heap object
        print("Changing heap contents...")
        if self.val_a == 1:
             self.heap_ref[0] = 99
        else:
            self.heap_ref[0] = "z"   
        print(f"Heap contents after modification: {self.heap_ref}")
        print(f"Heap reference ID again: {id(self.heap_ref)}") # Shows that the memory address remains the same
        print("Notice how the object itself stayed the same, but its contents changed.\n")

if __name__ == "__main__": # Main execution
    heap1 = [1, 2, 3]
    StackMathInstance1 = StackMath(*heap1)
    StackMathInstance1.startFunc()

    heap2 = ["a", "b", "c"]
    StackMathInstance2 = StackMath(*heap2)
    StackMathInstance2.startFunc()
