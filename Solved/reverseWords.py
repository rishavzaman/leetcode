class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split()
        for i in range(len(t)):
            t[i] = t[i][::-1]
        rev = ' '.join(t)
        return rev