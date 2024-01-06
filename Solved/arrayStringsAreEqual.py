class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # w1 = ''
        # for c in word1:
        #     w1 = w1+c
        # w2 = ''
        # for d in word2:
        #     w2 = w2+d
        # return w1 == w2
        return ''.join(word1) == ''.join(word2)