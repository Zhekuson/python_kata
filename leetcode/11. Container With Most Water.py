class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        s_max = 0
        while i < len(height) and j > i:
            s = (j - i) * min(height[i], height[j])
            if s > s_max:
                s_max = s
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return s_max