# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import Queue
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 如果当前节点为空
        if root is None:
            return "#_"  #下划线为每个节点值之间的分隔符
        # 先把头的值转换为字符串
        res = str(root.val) + "_"
        res += self.serialize(root.left)
        res += self.serialize(root.right)
        return res
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree = data.split("_")
        if len(tree) == 0:
            return None
        q = Queue()
        for i in tree:
            q.put(i)
        def process(q):         
            t = q.get()
            # 当前节点为#，则这棵树为空
            if t == '#':
                return None
            # 当前节点不为#，将队头节点作为头节点构造一棵树，并且获得它的左子树和右子树
            head = TreeNode(int(t))
            head.left = process(q)
            head.right = process(q)
            return head
        return process(q)
