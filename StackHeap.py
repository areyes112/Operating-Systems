import time
import tracemalloc

tracemalloc.start() # Start tracing memory allocations

class StackMath: # Demonstrates stack and heap behavior
    def __init__(self, val_a, val_b, val_c):
        self.val_a = val_a
        self.val_b = val_b
        self.val_c = val_c

        self.heap_ref = [val_a, val_b, val_c]

    def startFunc(self): # Initiates the stack demonstration
        print("\n=== Demonstrating Stack (LIFO) Behavior ===\n")
        self.funcA()
        time.sleep(1)
        print("\n=== Stack Unwinding Complete ===\n")

        time.sleep(1)
        print("\n=== Demonstrating Heap (Memory Storage) Behavior ===\n")
        self.showHeap()

    def funcA(self): # First function in the call stack
        print("========== Function A  =======\ \n")
        time.sleep(1) # Simulate some processing delay
        self.funcB()
        time.sleep(1)
        print("========== Function A  =======/ \n")

    def funcB(self): # Second function in the call stack
        print("========== Function B  ========\ \n")
        time.sleep(1)
        self.funcC()
        time.sleep(1)
        print("========== Function B  ========/ \n")

    def funcC(self): # Third function in the call stack
        print("========== Function C  =========\ \n")
        time.sleep(1)
        print(f"Values in local scope: {self.val_a}, {self.val_b}, {self.val_c}  | \n")
        time.sleep(1)
        print("========== Function C  =========/ \n")

    def showHeap(self): # Demonstrates heap behavior

        snapshot_heap1 = tracemalloc.take_snapshot()  # take a snapshot before heap operations
        print(f"Heap reference ID: {id(self.heap_ref)}") # This calls the memory address of the heap object
        current, peak = tracemalloc.get_traced_memory() # Get current and peak memory usage
        print(f"Current memory usage: {current / 10**6}MB; Peak: {peak / 10**6}MB") # Display memory usage
        print(f"Heap contents: {self.heap_ref}") #This shows the contents of the heap object
        print("Changing heap contents...")
        if self.val_a == 1:
             self.heap_ref[0] = 99
        else:
            self.heap_ref[0] = "z"   
        print(f"Heap contents after modification: {self.heap_ref}")
        print(f"Heap reference ID again: {id(self.heap_ref)}") # Shows that the memory address remains the same
        print("Notice how the object itself stayed the same, but its contents changed.\n")
        snapshot_heap2 = tracemalloc.take_snapshot()  # take another snapshot after heap operations
        stats_heap = snapshot_heap1.compare_to(snapshot_heap2, 'lineno')
        stats_heap = [stat for stat in stats_heap if "StackHeap.py" in str(stat.traceback)]
        print("=== Memory Allocation Stats During Heap Operations ===\n")
        for stat in stats_heap[:5]:
            print(stat)

if __name__ == "__main__": # Main execution

    snapshot_main1 = tracemalloc.take_snapshot()  # take a snapshot before creating instances

    heap1 = [1, 2, 3]
    StackMathInstance1 = StackMath(*heap1)
    StackMathInstance1.startFunc()

    heap2 = ["a", "b", "c"]
    StackMathInstance2 = StackMath(*heap2)
    StackMathInstance2.startFunc()

    snapshot_main2 = tracemalloc.take_snapshot()  # take another after creating second instance
    stats_main1 = snapshot_main2.compare_to(snapshot_main1, 'lineno')
    stats_main1 = [stat for stat in stats_main1 if "StackHeap.py" in str(stat.traceback)]
    print("\n=== Memory Allocation Stats After Running Main ===\n")
    for stat in stats_main1[:5]:
        print(stat)

tracemalloc.stop()