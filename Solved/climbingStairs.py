class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1

        
        for i in range(n+1):
            a, b = b, a+b
            i += 1
        return a

        