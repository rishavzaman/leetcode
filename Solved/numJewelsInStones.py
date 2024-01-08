class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # count = 0
        # for s in jewels:
        #     count += stones.count(s)
        # return count

        count = 0
        jlist = list(jewels)
        slist = list(stones)
        for i in jlist:
            count += slist.count(i)
        return count