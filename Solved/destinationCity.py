class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts, ends = map(set, zip(*paths))
        return (ends - starts).pop()