class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        srt = [x[0] for x in points]
        srt.sort()

        Max = 0

        for i in range(len(srt)-1):
            Max = max(Max, srt[i+1]-srt[i])

        
        return Max