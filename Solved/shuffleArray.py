class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        t = []
        split = len(nums) // 2
        for i in range(split):
            t.append(nums[i])
            t.append(nums[i+split])
        return t