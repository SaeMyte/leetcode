class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归实现
        res = []
        def inorder(root):
            if root == None:
                return None
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            return res
        return inorder(root)
# 非递归实现
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 非递归实现
        res = []
        stack = []
        while stack or root:
            # 先将所有子树的左边界进栈
            if root:  #当前节点不为空
              stack.append(root)
              root = root.left
            else:  #左边界全部进入栈
              #依次出栈
              root = stack.pop()
              #再将当前节点的右边界入栈
              res.append(root.val)
              root = root.right
        return res
