class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        # i = 0
        # num = 0
        # k = len(s)

        # while i < k:
        #     if i == k - 1:
        #         num += roman[s[i]]
        #         break
        #     if roman[s[i]] >= roman[s[i+1]]:
        #         num += roman[s[i]]
        #         i+=1
        #         continue
        #     if roman[s[i]] < roman[s[i+1]]:
        #         num += -roman[s[i]]
        #         i+=1
        #         continue

        # return(num)

        
        num = {}
        for i, n in enumerate(s):
            # num.append[i,roman[n]]
            num[i] = roman[n]
        for i in range(len(num)-1):
            if num[i] < num[i+1]:
                num[i] = -num[i]

            
        # return(num)
        return(sum(num.values()))


if __name__ == "__main__":
    S = Solution()
    result = S.romanToInt('MCMXCIV')
    print(result)