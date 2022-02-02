# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n - 1
        while left <= right :
            cur_idx = (left + right) // 2
            if isBadVersion(cur_idx):
                right = cur_idx - 1
            else:
                left = cur_idx + 1
        return right if right > left else left