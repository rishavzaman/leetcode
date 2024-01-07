class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for i, x in enumerate(encoded):
            arr.append(x ^ arr[i])
        return arr