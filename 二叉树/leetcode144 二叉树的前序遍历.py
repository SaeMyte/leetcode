# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def preorder(root):
            # 递归实现
            if root == None:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return res

# 非递归写法
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归实现
        result = []
        stack = []
        if root == None:
            return None
        stack.append(root)
        while stack:  #注意python判断list为空的写法 错误: while stack is not None
            # 弹出当前节点并且打印
            tmp = stack.pop()
            result.append(tmp.val)
            #将右孩子和左孩子压入栈中
            if tmp.right is not None:
                stack.append(tmp.right)
            if tmp.left is not None:
                stack.append(tmp.left)
        return result
