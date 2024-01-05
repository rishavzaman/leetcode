class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}


        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            # get allows a default value if the key s[i] does not exist
            countT[t[i]] = countT.get(t[i], 0) + 1
        for c in  countS:
            if countS[c] != countT.get(c,0):
                return False

        return True

# cheating methods
# return Counter(s) == Counter(t)
# return sorted(s) == sorted(t)

if __name__ == "__main__":
    S = Solution()
    print(S.isAnagram('asd','dsa'))