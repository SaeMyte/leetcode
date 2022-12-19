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
        #非递归实现
        #头节点先入栈
        res = []
        stack1 = []
        stack2 = []
        if root == None:
            return
        stack1.append(root)
        #当前节点弹出，按左、右节点入栈
        while stack1:
            tmp = stack1.pop()
            # 当前节点入第二个栈
            stack2.append(tmp)
            if tmp.left is not None:
                stack1.append(tmp.left)
            if tmp.right is not None:
                stack1.append(tmp.right)
        # 第二个栈中出栈顺序为：左、右、头
        while stack2:
            t = stack2.pop()
            res.append(t.val)
        return res
