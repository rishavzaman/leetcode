class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for x, i in enumerate(nums):
            if target - i in d:
                return([x, d[target-i]])
            d[i] = x
        
        # return(0)

if __name__ == "__main__":
    S = Solution()
    result = S.twoSum([2,7,11,15], 9)
    print(result)