class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def process(i, nums, res):
            if i == len(nums):
                res.append(nums[:])
                return 
            flag = set()  # 这里不能放在外面，从[i, len(nums)-1]中找一个放在i上，并且保证不重复
            for j in range(i, len(nums)):
                if nums[j] not in flag:  # 当前元素已经被试过了
                    flag.add(nums[j])
                    nums[i], nums[j] = nums[j], nums[i]
                    process(i+1, nums, res)
                    nums[i], nums[j] = nums[j], nums[i]
        process(0, nums, res)
        return res
