# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr= head
        count=0
        while curr:
            count+= 1
            curr= curr.next
        middle = count//2
        ptr= range(middle)
        curr= head
        for i in ptr:
            curr= curr.next
        return curr