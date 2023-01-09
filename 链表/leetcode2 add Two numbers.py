# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
最开始的代码
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        flag = 0 # 记录进位
        result = ListNode()
        p = result
        while p1 and p2:  # 前面相等的位相加
          plus = p1.val + p2.val + flag
          flag = int(plus) / int(10) if plus >= 10 else 0
          t = ListNode(int(plus%10), None)
          p.next = t
          p = p.next
          p1 = p1.next
          p2 = p2.next
        if p1 is not None:  # 如果p1不为空，所以p1还有剩的
          while p1:
              plus = p1.val + flag
              flag = int(plus) / int(10) if plus >= 10 else 0
              t = ListNode(int(plus%10), None)
              p.next = t
              p = p.next
              p1 = p1.next  
        if p2 is not None:
          while p2:
              plus = p2.val + flag
              flag = int(plus) / int(10) if plus >= 10 else 0
              t = ListNode(int(plus%10), None)
              p.next = t
              p = p.next
              p2 = p2.next
        # 最后如果有多的位
        if flag != 0:
            t = ListNode(int(flag), None)
            p.next = t
        return result.next
"""
优化一下
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        flag = 0 # 记录进位
        result = ListNode()
        p = result
        # 优化一下，不用单独判断p2和p1是否为空
        while p1 or p2: 
          n1 = p1.val if p1 else 0
          n2 = p2.val if p2 else 0
          plus = n1 + n2 + flag
          flag = int(plus) / int(10) if plus >= 10 else 0
          t = ListNode(int(plus%10), None)
          p.next = t
          p = p.next
          if p1:
              p1 = p1.next
          if p2:
              p2 = p2.next
        # 最后多的一位
        if flag != 0:
            t = ListNode(int(flag), None)
            p.next = t
        return result.next
