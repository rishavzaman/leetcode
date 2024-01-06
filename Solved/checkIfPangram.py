class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = [char for char in 'qwertyuiopasdfghjklzxcvbnm']
        for c in sentence:
            if c in s:
                s.remove(c)
        if s:
            return False
        else:
            return True