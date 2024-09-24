class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        mod = 10**9 + 7
        for _ in range(k):
            min_val = min(nums)
            min_index = nums.index(min_val)
            nums[min_index] = (min_val * multiplier) % mod
        return nums
