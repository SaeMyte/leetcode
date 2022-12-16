class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 链表只有一个元素也是回文链表
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        # 链表中有奇数个元素
        if fast.next == None:
            # 慢指针后面的进行逆序操作
            pre = None
            cur = slow.next
            slow = None  # 将中点指针置为None
        else: # 链表中有偶数个元素
            pre = None
            cur = slow.next
            slow.next = None
            # 逆置slow后面的链表
        while cur != None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        while head != None and pre!= None:
            if pre.val != head.val:
                return False
            else:
                pre = pre.next
                head = head.next
        return True
"""
第一次错误原因: 在进行回文判断时，pre最开始用的cur，但是此时的cur为None
"""
