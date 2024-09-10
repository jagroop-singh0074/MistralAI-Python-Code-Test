class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        left_product = 1
        right_product = 1
        for i in range(n):
            answer[i] *= left_product
            left_product *= nums[i]
            answer[n - i - 1] *= right_product
            right_product *= nums[n - i - 1]
        return answer
