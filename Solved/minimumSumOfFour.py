class Solution:
    def minimumSum(self, num: int) -> int:
        # num = str(num)
        # L = len(num)
        # Min = max(num)
        # for i in range(L-1):
        #     for j in (i+1,L-1):
        #         Min = min(int(Min),int(num[i])+int(num[j]))
        # return Min

        num = str(num)
        num = [int(x) for x in num]
        num.sort()
        num.reverse()
        return int(num[0]) + int(num[1]) + int(num[2])*10 + int(num[3])*10