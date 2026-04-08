class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # optimized prefix and suffix products 2 array

        n = len(nums)

        result = [1] * n

        prefix = 1
        for i in range (0, n):
            result[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            result[i] = result[i] * postfix
            postfix = postfix * nums[i]

        return result


"""
      nums = [1,2,4,6]
    prefix = [1,1,2,8]
    suffix = [48,24,6,1]
    result = [48,24,12,8]
"""
        