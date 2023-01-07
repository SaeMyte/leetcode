class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        sum = []
        tmp = 0
        # 求前缀和
        for i in nums:
            tmp += i
            sum.append(tmp)
        maxValue = 0
        stack = []
        # 求当前元素的左右第一个小于它的元素，单调递增栈
        # 有等于的情况，栈中使用链表
        for idx, value in enumerate(nums):
            while stack and nums[stack[-1][-1]] > value:
                indexArray = stack.pop()
                leftIndex = stack[-1][-1] if stack else -1  # 左边第一个比它小的
                rightIndex = idx # 右边第一个比它小的
                for i in indexArray:
                    # 计算累加和，此时不可能出现rightIndex为-1的情况
                    if leftIndex == -1:
                        curSum = sum[rightIndex] - value
                    else:
                        curSum = sum[rightIndex] - sum[leftIndex] - value
                    maxTmp = curSum * nums[i]
                    maxValue = max(maxTmp, maxValue)
                    #print(leftIndex, rightIndex, maxTmp)
            if stack and nums[stack[-1][-1]] == value:  # 如果栈顶=value
                stack[-1].append(idx)
            else:
                stack.append([idx])
        # 栈中剩余元素
        while stack:
            indexArray = stack.pop()
            leftIndex = stack[-1][-1] if stack else -1
            for i in indexArray:
                if leftIndex == -1:
                    curSum = sum[-1]
                else:
                    curSum = sum[-1] - sum[leftIndex]
                maxTmp = curSum * nums[i]
                maxValue = max(maxTmp, maxValue)
                #print(leftIndex, -1, maxTmp)
        return int(maxValue) % int(1e9 + 7)
