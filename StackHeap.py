from heapq import heapify, heappush, heappop   

class StackMath:
    def __init__(self,val_a,val_b,val_c):
        self.val_a = val_a
        self.val_b = val_b
        self.val_c = val_c

    def summation(self, n):
        total_a = 0
        total_b = 0
        total_c = 0
        for i in range(n + 1):
            total_a += self.val_a
            total_b += self.val_b
            total_c += self.val_c
        return total_a, total_b, total_c
    
    def factorial(self):
        def fact(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * fact(n - 1)
        return fact(self.val_a), fact(self.val_b), fact(self.val_c)

if __name__ == "__main__":

    num1 = StackMath(3, 4, 5)
    print("Factorials:", num1.factorial())
    
    