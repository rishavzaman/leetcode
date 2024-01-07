class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        while nums:
            Min1 = min(nums)
            nums.remove(Min1)
            Min2 = min(nums)
            nums.remove(Min2)
            arr.append(Min2)
            arr.append(Min1)
        return arr