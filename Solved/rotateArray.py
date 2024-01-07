class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # a = nums.copy()
        # L = len(nums)
        # for i in range(L):
        #     nums[i] = a[(i+L-k)%L]

        # n = k%len(nums)
        # tmp = nums[-n:] + nums[:-n]
        # for i in range(len(tmp)):
        #     nums[i] = tmp[i]

        n = k%len(nums)
        nums[:] = nums[-n:] + nums[:-n]