class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)

        # n1 = 0

        # e1 = 0
        # for i in num1[::-1]:
        #     n1 += int(i)*(10**e1)
        #     e1 += 1

        # e2 = 0
        # n2 = 0
        # for j in num2[::-1]:
        #     n2 += int(j)*(10**e2)
        #     e2 += 1
        
        
        # return str(n1+n2)

        # a = 0
        # b = 0
        # count = 0
        # for i, n in enumerate(num1):
        #     while str(count) != n:
        #         count += 1
        #     a += count * 10 ** (len(num1) - 1 - i)
        #     count = 0
        # for j, m in enumerate(num2):
        #     while str(count) != m:
        #         count += 1
        #     b += count * 10 ** (len(num2) - 1 - j)
        #     count = 0
        # return str(a+b)

        return str(int(num1)+int(num2))