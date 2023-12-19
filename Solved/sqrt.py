class Solution:
    def mySqrt(self, x: int) -> int:
        
        #basically binary search
        #initialize left and right sides
        L = 0
        R = x

        #compute mean then square it
        #shift endpoints based on difference
        while L <= R:
            M = (L+R) // 2

            if M * M > x:
                R = M - 1
            elif M * M < x:
                L = M + 1
            else:
                return M

        return R

if __name__ == "__main__":
    S = Solution()
    k = int(input())
    result = S.mySqrt(k)
    print(result)