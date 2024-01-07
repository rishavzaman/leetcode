class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        index = [0]*len(nums)

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] < nums[i]:
                    index[i] += 1
                elif nums[j] > nums[i]:
                    index[j] += 1
                    
        return index