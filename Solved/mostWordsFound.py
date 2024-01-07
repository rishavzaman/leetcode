class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        Max = 0
        for s in sentences:
            t = s.split()
            Max = max(Max,len(t))
        return Max