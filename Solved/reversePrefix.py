class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        i = word.find(ch)
        return word[i:0:-1] + word[0] + word[i+1:]