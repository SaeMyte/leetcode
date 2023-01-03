class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 先手函数
        def f(arr, L, R):
            # 如果只有一个元素了，先手就获得这个
            if L == R:
                return arr[L]
            # 否则，绝顶聪明的角度，获得两个选择更大值的那个
            return max(arr[L]+s(arr, L+1, R), arr[R]+s(arr, L, R-1))
        # 后手函数
        def s(arr, L, R):
            if L == R:
                # 作为后手拿不到
                return 0
            return min(f(arr, L+1, R), f(arr, L, R-1))
        # 玩家1先手，玩家2后手
        score1 = f(nums, 0, len(nums)-1)
        score2 = s(nums, 0, len(nums)-1)
        if score1 >= score2:
            return True
        else:
            return False
