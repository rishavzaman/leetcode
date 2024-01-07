class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L = 0
        R = 0
        count = 0

        for c in s:
            if c == 'L':
                L += 1
            else:
                R += 1
            if L == R:
                count += 1
                L == 0
                R == 0
                
        return count