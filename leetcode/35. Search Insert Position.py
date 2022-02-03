class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result_index = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            cur_idx = (left + right) // 2
            if nums[cur_idx] == target:
                return cur_idx
            elif nums[cur_idx] > target:
                right = cur_idx - 1
            else:
                left = cur_idx + 1

        return left