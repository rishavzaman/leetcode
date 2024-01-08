class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # answer = []
        # for i in range(1,n+1):
        #     if i % 15 == 0:
        #         answer.append("FizzBuzz")
        #     elif i % 3 == 0:
        #         answer.append("Fizz")
        #     elif i % 5 == 0:
        #         answer.append("Buzz")
        #     else:
        #         answer.append(str(i))
        # return answer

        ans = [str(x+1) for x in range(n)]
        for i in range(2, n, 3):
            ans[i] = "Fizz"
        for j in range(4, n, 5):
            ans[j] = "Buzz"
        for k in range(14, n, 15):
            ans[k] = "FizzBuzz"
        return ans