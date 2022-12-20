import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.preValue = -sys.maxint - 1  #记录前面的值，初始化为最小值
        self.flag = 1
        # 二叉搜索树中序一定是升序
        def inorderTrasval(root):
            global flag
            if root == None:
              return True  #空树也是二叉搜索树
            inorderTrasval(root.left)
            if root.val<=self.preValue:
                self.flag = 0
                return 
            else:
                self.preValue = root.val
            inorderTrasval(root.right)
        inorderTrasval(root)
        if self.flag == 1:
            return True
        return False
