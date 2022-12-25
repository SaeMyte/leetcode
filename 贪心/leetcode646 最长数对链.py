class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        sortList = sorted(pairs,key = lambda pairs:pairs[1])
        curEndtime = sortList[0][1]
        result = 1
        for i in range(1, len(sortList)):
            if sortList[i][0] > curEndtime:
                result += 1
                curEndtime = sortList[i][1]
        return result
