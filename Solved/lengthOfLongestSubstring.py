class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dic = {}
        # length = 0
        # for c in s:
        #     if c not in dic:
        #         dic[c] = 1
        #         length +=1
        #     else:
        #         dic.clear()
        #         length = 0
         
        dic = {}
        l = 0
        length = 0
        for r in range(len(s)):
            c = s[r]
            if c in dic and dic[c] >= l:
                l = dic[c] + 1
            else:
                length = max(length, r - l + 1)
            dic[c] = r


        return length