class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        
        if valueDiff == 0:
            dict = {}
            for i, n in enumerate(nums):
                if n in dict:
                    if abs(dict[n] - i) <= indexDiff:
                        return True
                    else:
                        dict = {}
                        dict[n] = i
                else:
                    dict[n] = i
            return False


        dict = {}
        for i, n in enumerate(nums):
            for j in dict:
                if abs(dict[j] - i) <= indexDiff:
                    if abs(j - n) <= valueDiff:
                        return True
                    else:
                        continue
                else:
                    continue
            dict[n] = i



        return False