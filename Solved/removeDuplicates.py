class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # count = 0
        # dic = {}
        # i = 0
        # L = len(nums)
        # for i,n in enumerate(nums):
        #     if n in dic:
        #         nums.remove(n)
        #         i -= 1
        #     else:
        #         dic[n] = i
        # while i < L:
        #     if nums[i] in dic:
        #         nums.remove(nums[i])
        #         i -= 1
        #     else:
        #         dic[nums[i]] = i
        #     i += 1

        # i = 0
        # dic = {}
        # for n in nums:
        #     if n not in dic:
        #         nums[i] = n
        #         i += 1
        #     else:
        #         dic[n] = i

        j = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[j] = nums[i]
                j += 1
        return j