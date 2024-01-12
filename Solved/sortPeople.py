class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data = zip(heights,names)
        sorted_data = sorted(data, reverse=True)
        return [name for height, name in sorted_data]