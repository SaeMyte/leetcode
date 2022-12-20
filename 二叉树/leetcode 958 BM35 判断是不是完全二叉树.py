# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 
# @return bool布尔型
#
import queue
class Solution:
    def isCompleteTree(self , root: TreeNode) -> bool:
        # write code here
        # 层序遍历
        q = queue.Queue()
        if root == None:
            return False
        q.put(root)
        isleaf = False
        while not q.empty():
            tmp = q.get()
            if isleaf:  #这个开关打开的话，当前节点必须是叶子节点
                if tmp.left is not None or tmp.right is not None:
                    return False
            else:  #没打开开关
                # 如果当前节点的左节点为空而右节点不为空，则肯定不是完全二叉树
                if tmp.left is None and tmp.right is not None:
                    return False
                elif (tmp.left is not None and tmp.right is None) or (tmp.left is None and tmp.right is None):    
                    isleaf = True
                # 否则如果当前节点孩子不是双全：左节点为空，右节点不为空，或者都为空，后面的节点一定是叶子节点
                # 相当于一个开关，后面的节点必须全为叶子节点   
            
            if tmp.left is not None:
                q.put(tmp.left)
            if tmp.right is not None:
                q.put(tmp.right)
        return True
    
