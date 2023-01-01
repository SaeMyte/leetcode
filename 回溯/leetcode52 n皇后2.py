class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        record = [-1]*n  # 用来记录第i行皇后所在的纵坐标
        def isValid(record, i, j): # 当前第i行皇后是否能放第j列
          for k in range(0, i):
              # 不能同列
              if record[k] == j:
                  return False
              # 也不能在对角线上
              if abs(record[k] - j) == abs(k - i):
                  return False
          return True
        def process(record, i, n):
            # 遍历到最后一行的下一行，说明找到了一种方法
            if i == n:
                return 1
            res = 0
            for k in range(0, n):  # 当前第i行皇后在n个j列中依次检查
                if isValid(record, i, k):
                    # 处理节点
                    record[i] = k
                    # 继续向下遍历
                    res += process(record, i+1, n)
                    # 恢复处理结果
                    record[i] = -1
            return res
        return process(record, 0, n)
