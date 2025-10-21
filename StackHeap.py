from heapq import heapify, heappush, heappop   
from collections import deque

if __name__ == "__main__":
    # Demonstration of Stack using deque
    stack = deque()
    
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print("Stack pop:", stack.pop())  # Outputs: 3

    # Demonstration of Heap using heapq
    heap = []
    heapify(heap)

    heappush(heap, 5)
    heappush(heap, 1)
    heappush(heap, 3)
    print("Heap pop:", heappop(heap))  # Outputs: 1