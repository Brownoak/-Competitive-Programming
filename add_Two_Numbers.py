# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr= temp = ListNode(0)
        holder = 0

        while holder or l1 or l2:
          if l1:
            holder += l1.val
            l1 = l1.next
          if l2:
            holder += l2.val
            l2 = l2.next
          curr.next = ListNode(holder % 10)
          holder //= 10
          curr = curr.next

        return temp.next