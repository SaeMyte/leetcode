class Solution(object):
    def hanota(self, A, B, C):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :rtype: None Do not return anything, modify C in-place instead.
        """
        def process(i, start, end, other):
            # basecase
            if i == 1:
                tmp = start.pop() # 这里容易出错，是小的先出来，所以是从list尾出来而不是头    
                end.append(tmp)
            else:
                # 将1~i-1移动到other
                process(i-1, start, other, end)
                # 将第i个移动到end中
                tmp = start.pop()
                end.append(tmp)
                # 再将1~i-1从other移动到end上
                process(i-1, other, end, start)
        n = len(A)
        process(n, A, C, B)
