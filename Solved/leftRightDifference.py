class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        ans = [0]*len(nums)
        for i,n in enumerate(nums):
            right -= n
            ans[i] = abs(left-right)
            left += n
        return ans