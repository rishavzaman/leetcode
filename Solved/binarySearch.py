class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            # middle = (left + right) // 2
            middle = left + ( (right - left) // 2 ) # faster
            if nums[middle] == target:
                return middle
            if nums[middle] <  target:
                left = middle + 1
            if nums[middle] > target:
                right = middle - 1
        return -1