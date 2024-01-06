class Solution:
    def isUgly(self, n: int) -> bool:
        fact = []
        d = 2
        while d*d <= n:
            while n%d == 0:
                fact.append(d)
                n //= d
            d += 1
        for i in fact:
            if i == 2 or i == 3 or i == 5:
                fact.remove(i)
        if fact == []:
            return True
        else:
            return False
