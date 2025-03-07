class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4 -1 -1 0 1 2
        nums = sorted(nums)
        result = set()
        for middle in range(1, len(nums) - 1):
            p1 = 0
            p2 = len(nums) - 1
            while p1 < middle < p2:
                if nums[p1] + nums[p2] + nums[middle] > 0:
                    p2 -= 1
                elif nums[p1] + nums[p2] + nums[middle] < 0:
                    p1 += 1
                else:
                    result.add((nums[p1], nums[middle], nums[p2]))
                    p2 -= 1
                    p1 += 1
        res = []
        for item in result:
            res.append([item[0], item[1], item[2]])
        return res
