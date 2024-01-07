class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return(False)
        
        # # y=0
        # # for i in len(x):
        # #     y+=x//10^i
        
        # # return(y)

        # # i=0
        # # while True:
        # #     y+=x//10^

        # s = str(x)
        # y = s[::-1]
        # return(int(y) == x)

        return str(x) == str(x)[::-1]







if __name__ == "__main__":
    S = Solution()
    result = S.isPalindrome(1234321)
    print(result)