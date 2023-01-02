class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # res存放所有可能的结果
        def process(i, nums, res):
          if i == len(nums):
              res.append(nums[:]) # 易错，不能写成res.append(nums)，是浅拷贝
              return 
          for j in range(i, len(nums)):
              nums[i], nums[j] = nums[j], nums[i]
              process(i+1, nums, res)
              nums[i], nums[j] = nums[j], nums[i]
        process(0, nums, res)
        return res
