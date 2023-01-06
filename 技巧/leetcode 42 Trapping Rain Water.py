"""
错误
MaxValue = [[-1,-1]]*len(height)  这样创建，修改MaxValue[0][1]，所有的[1]均会被修改。
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        help = []  # 单调递减栈
        for i, value in enumerate(height):
            while help and height[help[-1]] < value: # 此时开始记录
              index = help.pop()
              # 左边离它最大的此时是栈顶
              if help:
                  L = help[-1]
                  R = i
                  MinValue = min(height[R], height[L])
                  MinValue = min(MinValue, MinValue - height[index])
                  water += (R- L -1)*MinValue
            help.append(i)
        return water
