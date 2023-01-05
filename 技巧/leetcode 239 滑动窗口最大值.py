"""
MyCode
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []  # 存放窗口的最大值
        help = []
        for i in range(0, k):
            if not help:  # 第二次犯错了，判断list 为空不能用None
                help.append(i)
            else:
                j = len(help) - 1
                while j >= 0 and nums[help[j]] <= nums[i]:
                    help.pop()
                    j -= 1
                help.append(i)
        res.append(nums[help[0]])
        for i in range(k, len(nums)):
            # 每一次L和R都向后移动
            # L动
            if help[0] == i - k:
                help.pop(0)
            # R动
            if not help:  # 第二次犯错了，判断list 为空不能用None
                help.append(i)
            else:
                j = len(help) - 1
                while j >= 0 and nums[help[j]] <= nums[i]:
                    help.pop()
                    j -= 1
                help.append(i)
            res.append(nums[help[0]])
        return res
      
  class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []  # 存放窗口的最大值
        help = []
        for i, value in enumerate(nums):
            while help and nums[help[-1]] <= value:
                help.pop()
            help.append(i)
            # L动
            if i - k == help[0]:
                help.pop(0)
            # R动
            if i >= k-1:
                res.append(nums[help[0]])
        return res
