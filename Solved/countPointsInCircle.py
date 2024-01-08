class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for q in queries:
            count = 0
            for p in points:
                if ((p[0]-q[0])**2 + (p[1]-q[1])**2) <= q[2]**2:
                    count += 1
            ans.append(count)
        return ans