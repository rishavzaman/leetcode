class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        Max = max(candies)
        res = []
        for c in candies:
            res.append(c + extraCandies >= Max)
        return res