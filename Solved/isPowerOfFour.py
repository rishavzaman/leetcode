class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        k = 1
        while k <= n:
            if k == n:
                return True
            k *= 4
        return False