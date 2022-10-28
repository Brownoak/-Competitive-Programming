# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        container = []
        curr = head
        while curr:
            container.append(curr.val)
            curr = curr.next
        start = 0
        end = len(container) - 1
        while end >= start:
            if container[end] == container[start]:
                start += 1
                end -= 1
            else: return False
            
        return True