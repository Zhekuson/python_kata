class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = set()
        for i in range(len(nums)):
            if not nums[i] in result:
                result.add(nums[i])
        for i, item in enumerate(sorted(result)):
            nums[i] = item
        return len(result)