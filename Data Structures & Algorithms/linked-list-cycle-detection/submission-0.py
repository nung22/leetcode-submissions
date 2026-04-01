# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        vals = []

        while curr.next:
            if curr.val in vals:
                return True
            vals.append(curr.val)
            curr = curr.next
        
        return False