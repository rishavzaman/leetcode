class Solution:
    def isHappy(self, n: int) -> bool:
        while(len(str(n)) > 1):
            sum = 0
            for i in str(n):
                sum += int(i) ** 2
            n = sum
        if n == 1 or n == 7:
            return True
        else:
            return False