class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float('-inf')
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if i >= k:
                curr_sum -= nums[i - k]
            if i >= k - 1:
                max_sum = max(max_sum, curr_sum)
        return max_sum / k
