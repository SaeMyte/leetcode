class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 存放第i行皇后的位置，放在了第几列
        board = [['.'] * n for _ in range(n)]  # 棋盘
        res = []  # 存放最终结果
        # 第i行皇后放在了j列是否可以
        def isValid(board, i, j):
            # 检查前i-1列
            for k in range(0, i):
                # 在同一列的不行
                if board[k][j] == 'Q':
                    return False
            # 斜对角线的也不行
            row = i - 1
            col = j - 1
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1
            row = i - 1
            col = j + 1
            while row >= 0 and col < len(board):
                if board[row][col] == 'Q':
                    return False
                row -= 1
                col += 1
            return True
        def process(i, board, n):  # 前i-1行都摆好了目前这一行该怎么摆
            if i == n: #到了最后一行的下一行，结束，保存结果
              tmp = []
              for data in board:
                  tmp_str = "".join(data)
                  tmp.append(tmp_str)
              res.append(tmp)
              return
            # 否则找当前行的解
            for j in range(0, n):  # 当前行是否能放在j列上
              if isValid(board, i, j):
                  # 更新board
                  board[i][j] = 'Q'
                  process(i+1, board, n)
                  board[i][j] = '.'
        process(0, board, n)
        return res
