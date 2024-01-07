class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for s in jewels:
            count += stones.count(s)
        return count