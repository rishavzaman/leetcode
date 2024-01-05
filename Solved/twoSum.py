class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, val in enumerate(nums):
            if target - val in d:
                return([i, d[target-val]])
            d[val] = i
        
        # return(0)

if __name__ == "__main__":
    S = Solution()
    result = S.twoSum([2,7,11,15], 9)
    print(result)