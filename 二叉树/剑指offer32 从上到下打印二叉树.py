#二叉树的层序遍历/宽度优先遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import Queue
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        # 层序遍历
        if root == None:
            return res
        q = Queue()
        q.put(root)
        while not q.empty():
            tmp = q.get()
            res.append(tmp.val)
            if tmp.left is not None:
                q.put(tmp.left)
            if tmp.right is not None:
                q.put(tmp.right)
        return res
