class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        L = len(words)
        count = 0
        for i in range(L):
            for j in range(i+1,L):
                if words[i] == words[j][::-1]:
                    count += 1
        return count