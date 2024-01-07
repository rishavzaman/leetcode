class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        non = [char for char in 'qwertyuiopasdfghjklzxcvbnm'+'1234567890']
        # none = [char for char in '~!@#$%^&*()_+:"?><|`-=[];/.,' + '\'' + ' ' + '\"' + '\\' + '{' + '}']
        for c in s:
            if c not in non:
                s = s.replace(c,'')

        return s == s[::-1]