class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        if len(nums) == 0:
            return -1
        for data in nums:
            result = result ^ data
        return result
