# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # 使用一个sH，sT节点，来表示小于x的链表的头指针和尾指针，遍历链表，当当前元素<x时，将它放入到小于链表中，并且从原链表中进行删除操作
        spre = None
        s = None
        ebh = None
        ebt = None
        # 链表中只有一个元素或者为空，则直接返回head
        if head == None or head.next == None:
            return head
        p = head
        while p != None:
            tmp = ListNode(p.val)
            if tmp.val < x:
                if spre == None:
                    spre = tmp
                    s = spre
                else:
                    s.next = tmp
                    s = tmp
            else:
                if ebh == None:
                    ebh = tmp
                    ebt = ebh
                else:
                    ebt.next = tmp
                    ebt = tmp
            p = p.next
        if spre == None:  # 没有小于x的元素
            head = ebh
        else:
            head = spre
            s.next = ebh
        return head
