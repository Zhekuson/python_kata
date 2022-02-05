class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left = 0
        right = N - 1
        # search middle
        while left <= right:
            cur_idx = (left + right) // 2
            if nums[cur_idx] == 0:
                right = cur_idx
                break
            elif nums[cur_idx] > 0:
                right = cur_idx - 1
            else:
                left = cur_idx + 1
        middle = max(left, right)
        left_arr = [x ** 2 for x in nums[:middle]]
        right_arr = [x ** 2 for x in nums[middle:]]

        left_idx = len(left_arr) - 1
        right_idx = 0
        nums = []
        while len(nums) < N:
            if left_idx >= 0 and right_idx < len(right_arr):
                if left_arr[left_idx] <= right_arr[right_idx]:
                    nums.append(left_arr[left_idx])
                    left_idx -= 1
                else:
                    nums.append(right_arr[right_idx])
                    right_idx += 1
            elif left_idx >= 0:
                nums.append(left_arr[left_idx])
                left_idx -= 1
            else:
                nums.append(right_arr[right_idx])
                right_idx += 1

        return nums









