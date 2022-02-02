class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result_index = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            cur_idx = (left + right) // 2
            if nums[cur_idx] == target:
                result_index = cur_idx
                break
            elif nums[cur_idx] < target:
                left = cur_idx + 1
            else:
                right = cur_idx - 1
        return result_index