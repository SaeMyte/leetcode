class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        max_width = -1
        res = [[root, 1]]
        while res:
            tmp = []  #存储每一层的节点下一层孩子和索引
            for tree, index in res:
                if tree.left:
                    tmp.append([tree.left, index*2])
                if tree.right:
                    tmp.append([tree.right, index*2+1])
            # 一层遍历完
            max_width = max(max_width, res[-1][1]- res[0][1]+1)
            res = tmp
        return max_width
