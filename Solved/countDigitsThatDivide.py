class Solution:
    def countDigits(self, num: int) -> int:
        # i = 2
        # count = 1
        # while i < num:
        #     if num % i == 0:
        #         count += 1
        #     i += 1
        # return count

        count = 0
        for n in str(num):
            if num % int(n) == 0:
                count +=1
        return count