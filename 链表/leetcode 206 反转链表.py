# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        # 至少有一个元素
        L = ListNode()
        while head != None:
            p = ListNode(head.val)
            # 错误写法 p = head  这里改变p的next地址，head的地址也将会改变
            p.next = L.next
            L.next = p
            head = head.next
        return L.next
