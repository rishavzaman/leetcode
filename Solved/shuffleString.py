class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t = [""]*len(s)
        for i,j in enumerate(indices):
            t[j] = s[i]
        return ''.join(t)