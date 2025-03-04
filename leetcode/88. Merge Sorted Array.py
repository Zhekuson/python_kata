# УЖАСНОЕ РЕШЕНИЕ, но оно зашло
class Solution:

    def spec_min(self, a, b):
        return (0, a) if a < b else (1, b)

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        i = m + n
        p1 = 0
        p2 = 0
        if m == 0:
            for j in range(n):
                nums1[j] = nums2[j]
            return
        if n == 0:
            return
        while i > 0:
            if p1 < m and p2 < n:
                pos, number = self.spec_min(nums1[p1], nums2[p2])
            elif p1 < m:
                pos = 0
                number = nums1[p1]
            elif p2 < n:
                pos = 1
                number = nums2[p2]

            result.append(number)
            if pos == 0:
                p1 += 1
            else:
                p2 += 1

            i -= 1
        # print(result)
        for i in range(len(result)):
            nums1[i] = result[i]
