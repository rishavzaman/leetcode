import math

class Solution:
    def isUgly(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        # fact = []
        # d = 2
        # while d <= n:
        #     if n%d == 0:
        #         fact.append(d)
        #         n //= d
        #     else:
        #         d += 1
        # i = 0
        # while i < len(fact):
        #     if fact[i] == 2 or fact[i] == 3 or fact[i] == 5:
        #         fact.remove(fact[i])
        #         i -= 1
        #     i += 1
        # if fact == []:
        #     return True
        # else:
        #     return False



        # if n <= 0:
        #     return False
        # fact = []
        # while n % 2 == 0:
        #     fact.append(2)
        #     n = n // 2
        # for d in range(3,int(math.sqrt(abs(n)))+1,2):
        #     while n % d == 0:
        #         fact.append(d)
        #         n = n // d
        # if n > 2:
        #     fact.append(n)

        # i = 0
        # while i < len(fact):
        #     if fact[i] == 2 or fact[i] == 3 or fact[i] == 5:
        #         fact.remove(fact[i])
        #         i -= 1
        #     i += 1
        # if fact == []:
        #     return True
        # else:
        #     return False


        # fact = []
        # d = 2
        # while d*d <= n:
        #     while n%d == 0:
        #         fact.append(d)
        #         n //= d
        #     d += 1
        # for i in fact:
        #     if i == 2 or i == 3 or i == 5:
        #         fact.remove(i)
        # if fact == []:
        #     return True
        # else:
        #     return False

        while n >= 1:
            if n%2 == 0:
                n = n//2
            elif n%3 == 0:
                n = n//3
            elif n%5 == 0:
                n = n//5
            elif n == 1:
                return True
            else:
                return False