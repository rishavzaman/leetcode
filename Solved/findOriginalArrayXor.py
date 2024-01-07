class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]

        i = 1
        L = len(pref)
        while i < L:
            arr.append(pref[i-1] ^ pref[i])
            i += 1

        return arr