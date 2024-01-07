class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for i, n in enumerate(nums):
            if n in dict:
                if abs(dict[n]-i) <= k:
                    return True
                else:
                    dict[n] = i
            else:
                dict[n] = i
        return False