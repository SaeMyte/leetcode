class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        # 尽可能用单元数量大的把卡车填满
        boxSort = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        v = 0
        for num, value in boxSort:
            if truckSize >= num:
                v += (num*value)
                truckSize -= num
            else:
                v += (truckSize*value)
                break
        return v 
