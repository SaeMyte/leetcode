# 错误做法
import heapq
class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        length = [0]*(len(cuts)+1)
        # 将cut排序，获得截断的每节木头长度
        cuts = sorted(cuts)
        for i in range(0, len(cuts)+1):
            if i == 0:
                length[i] = cuts[i]
            elif i == len(cuts):
                length[i] = n-cuts[i-1]
            else:
                length[i] = cuts[i] - cuts[i-1]
        # 准备一个小根堆
        print(length)
        heap = []
        for data in length:
            heapq.heappush(heap, data)
        sum = 0 # 记录代价
        while len(heap) > 1: # 得保证小根堆中至少有两个元素
            # 弹出两个
            cur = heapq.heappop(heap) + heapq.heappop(heap)
            print(sum,cur)
            sum += cur
            # 将相加的新的重新压入堆中
            heapq.heappush(heap, cur)
        return sum
 """
 以上做法通过不了，和分割金条问题不同，那道题目给出的是需要最终分割成的长度，但是这道题目规定了下刀的位置，不能只是简单通过长度来解答。不可以用贪心方法做
 """
