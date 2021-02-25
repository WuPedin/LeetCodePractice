class Solution:
    def fib(self, n: int) -> int:
        
        # Check 
        if n < 0:
            return -1
        
        # Recursive
        if n == 0:
            return 0
        if n== 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
        