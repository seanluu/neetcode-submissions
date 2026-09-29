# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # set both pointers to start at the same point as each other
        slow, fast = head, head 

        while fast and fast.next: # if no cycle, fast hits the end and loop exits naturally
            slow = slow.next # slow only goes up 1 node at a time
            fast = fast.next.next # fast goes up 2 nodes at a time

            # fast gains exactly 1 step on slow every iteration (2 steps vs 1).
            # if there's a cycle, they're both stuck looping inside it forever,
            # so that shrinking gap must eventually hit 0 — meaning they collide
            if slow == fast:
                return True

        return False # otherwise, we do not have a cycle