class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        f = [0]*N
        f[0] = nums[0]
        if N == 1:
            return f[0]
        f[1] = max(nums[1], nums[0])
        for i in range(2, N):
            f[i] = max(nums[i]+ f[i-2], f[i-1])
        return f[N-1]