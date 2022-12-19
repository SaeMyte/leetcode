# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #递归实现
        res = []
        def postorder(root):
            if root == None:
                return None
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return res
      
# 非递归实现
