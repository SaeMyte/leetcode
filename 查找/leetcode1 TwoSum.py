class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, value in enumerate(nums):
            if target - value in hashtable:
                return [hashtable[target - value], i]
            hashtable[value] = i 
