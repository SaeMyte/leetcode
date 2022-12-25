"""
# Mycode
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        # 贪心：工人完成他能力范围内最大利润的工作
        # 将利润按从高到低加入一个list，然后查询当前这份工作这个工人是否能完成，不能完成找下一个能完成的工作
        profit_dif = []  # 存储按利润排序后的利润和难度
        for i, pro in enumerate(profit):
            profit_dif.append([pro, difficulty[i]])
        print(profit_dif)
        # 按照利润进行排序
        profit_sort = sorted(profit_dif, key = lambda x: x[0], reverse = True)
        sum = 0
        for i in worker: #给每个工人找到适合它的工作
          for j in profit_sort:
              if i >= j[1]:
                  sum += j[0]
                  break
        return sum
"""
        class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        # 贪心：工人完成他能力范围内最大利润的工作
        # 将利润按从高到低加入一个list，然后查询当前这份工作这个工人是否能完成，不能完成找下一个能完成的工作
        job = zip(difficulty, profit)
        job = sorted(job)  # sort没有返回值， sorted有返回值    
        sum = i = best = 0
        for power in sorted(worker): #给每个工人找到适合它的工作
          while i < len(job) and power >= job[i][0]:
              best = max(best, job[i][1])
              i += 1
          sum += best
        return sum
