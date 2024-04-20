class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cur_sum = sum(nums[:k])
        max_sum = cur_sum
        for i in range(1, n - k + 1, 1):
            cur_sum = cur_sum - nums[i - 1] + nums[i - 1 + k]
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum / k