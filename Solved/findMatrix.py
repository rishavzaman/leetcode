class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # t = [[nums[0]]]
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         t.append([nums[i]])
        #     else:
        #         for k in range(len(t)):
        #             if nums[i] not in t[k]:
        #                 t[k].append(nums[i])
        # return t

        

        count = {}
        ans = []
        for n in nums:
            if n not in count:
                count[n] = 0
            i = count[n]
            if i == len(ans):
                ans.append([])
            ans[i].append(n)
            count[n] += 1
        return ans