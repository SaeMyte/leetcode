# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 递归函数的返回值，返回这棵树是否是平衡树，高度是多少
        def process(root):
            if root is None:
              return True, 0
            left_balance, left_height = process(root.left)
            right_balance, right_height = process(root.right)
            height = max(left_height, right_height) + 1
            if left_balance and right_balance and abs(left_height-right_height) < 2:
                balance = True
            else:
                balance = False
            
            return balance, height
        result, height = process(root)
        return result
