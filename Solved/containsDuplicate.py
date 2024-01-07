class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i, n in enumerate(nums):
            if n in dict:
                return True
            else:
                dict[n] = i
        return False