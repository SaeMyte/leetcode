class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0  
        left = 0  #记录小于区域的最后一个数
        right = len(nums)-1 #记录大于区域的前一个指针
        while i<= right:   #注意循环边界条件
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2 :
                nums[right], nums[i] = nums[i],nums[right]
                right -= 1
            else:
                i += 1
