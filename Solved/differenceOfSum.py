class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        Sum = sum(nums)
    
        dsum = 0
        for n in nums:
            for d in str(n):
                dsum += int(d)

        return abs(Sum-dsum)