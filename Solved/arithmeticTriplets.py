class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0

        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         for k in range(j,len(nums)):
        #             if nums[j]-nums[i]==diff and nums[k]-nums[j]==diff:
        #                 count+=1
    
        for i in range(len(nums)):
            if nums[i]+diff in nums and nums[i]+2*diff in nums:
                count += 1

        return count