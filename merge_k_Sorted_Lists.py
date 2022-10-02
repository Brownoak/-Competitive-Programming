# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:   
            heap=[]
            for i in lists:
                while i != None:
                    heap.append(i.val)
                    i= i.next
            if heap:
                heap.sort()
                root= ListNode(0)
                l= root
                for i in range(len(heap)):
                    l.next= ListNode(heap[i])
                    l=l.next
                return root.next