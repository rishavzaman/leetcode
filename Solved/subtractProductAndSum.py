from math import prod

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Sum = sum(map(int,str(n)))
        Prod = prod(map(int,str(n)))


        return Prod - Sum