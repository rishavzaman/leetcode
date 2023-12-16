class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")": "(", "}": "{", "]": "["}

        
        for char in s:
            if char in dic:
                # if stack:
                #     top = stack.pop()
                # else: continue
                # if top != dic[char]:
                #     return False
                top = stack.pop() if stack else '#'
                if dic[char] != top:
                    return False
                    # I understand now
                    # if stack else '#' just reorders things
                    # we need to check if stack is nonempty, then if pop corresponds
                    # but if we use the if else syntax, then we never check it
            else:
                stack.append(char)
        return not stack
                












if __name__ == "__main__":
    S = Solution()
    result = S.isValid("()[]{}")
    print(result)