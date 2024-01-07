class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        if rev < -(2**31) or rev > (2**31-1):
            return 0
        if x < 0:
            return -rev
        else:
            return rev