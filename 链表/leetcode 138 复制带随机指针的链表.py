"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:  #链表中没有节点
            return head
        # 在每一个老链表节点后，插入一个相同值的新节点
        p = head
    
        while p != None:
            tmp = ListNode(p.val)
            tmp.next = p.next
            p.next = tmp
            p = p.next.next
        # 依次遍历链表，完成rand指针
        p = head
        while p != None:
            q = p.next
            if p.random != None:
                q.random = p.random.next
            else:
                q.random = None
            p = p.next.next
        # 拿出复制的新节点，组成一个新链表
        newList = head.next
        p = head
        while p != None:
            next = p.next.next
            pcopy = p.next
            p.next = next
            if next == None:
                pcopy.next = None
            else:
                pcopy.next = next.next
            p = next 
        return newList
