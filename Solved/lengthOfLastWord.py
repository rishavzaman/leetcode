class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        last = 0
        for c in s[::-1]:
            if last == 1:
                if c == ' ':
                    break
                else:
                    count +=1
            else:
                if c == ' ':
                    continue
                else:
                    last = 1
                    count +=1
        return count