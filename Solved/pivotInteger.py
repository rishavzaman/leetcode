class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        for i in range(1,n):
            # if (i*(i+1) + (i-1)*i)//2== K:
            #     return i
            # i^2 + i + i^2 -i
            # if i**2 == K:
            #     return i
            if 2*i**2 == n*(n+1):
                return i
        return -1