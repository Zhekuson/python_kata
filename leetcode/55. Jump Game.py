class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        max_arrival = 0
        i = 0
        while i < N:
            if i <= max_arrival:
                if i + nums[i] > max_arrival:
                    max_arrival = i + nums[i]
            else:
                return False
            i += 1
        if max_arrival < N - 1:
            return False
        else:
            return True

