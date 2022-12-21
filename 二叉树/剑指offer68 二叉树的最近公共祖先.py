# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# p和q一定属于这棵树
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def process(root, p, q):
            if root is None or root == p or root == q:  # 当前节点为p或q，则p或q就是最低公共祖先
              return root           
            l = process(root.left, p, q)
            r = process(root.right, p, q)
            if l is not None and r is not None:  # p和q来自两棵树
              return root
            if l is not None:
              return l
            if r is not None:
              return r
        return process(root, p, q)
