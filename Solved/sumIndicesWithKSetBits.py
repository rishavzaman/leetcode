class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        t = [bin(x) for x in range(0,len(nums))]
        Sum = 0
        for i in t:
            if i.count('1') == k:
                Sum += nums[int(i,2)]
        return Sum