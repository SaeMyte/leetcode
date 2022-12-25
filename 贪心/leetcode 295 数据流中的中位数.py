import heapq
class MedianFinder(object):

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.maxHeap) == 0:
            heapq.heappush(self.maxHeap, -num)
        else:
            # 如果当前值小于等于大根堆，入大根堆，否则入小根堆
            if num <= -self.maxHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)
    def findMedian(self):
        """
        :rtype: float
        """
        len1 = len(self.maxHeap)
        len2 = len(self.minHeap)
        while abs(len1 - len2) > 1 :
            if len1 > len2:  # 大根堆的元素个数比小根堆元素个数多
              num = heapq.heappop(self.maxHeap)
              heapq.heappush(self.minHeap, -num)
            else:
              num = heapq.heappop(self.minHeap)
              heapq.heappush(self.maxHeap, -num)
            len1 = len(self.maxHeap)
            len2 = len(self.minHeap)
        if len1 == len2:
            result = (self.minHeap[0] - self.maxHeap[0])/2.0
        else:
            result = -self.maxHeap[0] if len1 > len2 else self.minHeap[0]
        return result
