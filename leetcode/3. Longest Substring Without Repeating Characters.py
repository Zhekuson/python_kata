class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        current = set()
        max_len = 0
        while right < len(s):
            if s[right] in current:
                current.discard(s[left])
                left += 1
            else:
                current.add(s[right])
                if len(current) > max_len:
                    max_len = len(current)
                right += 1
        return max_len
