# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # start both pointers at the same spot
        slow, fast = head, head

        # if there's no cycle, fast hits the end and loop exits naturally 
        # fast jumps 2, so both have to exist; if not, we hit the end, no cycle
        while fast and fast.next:
            slow = slow.next # goes up 1 node
            fast = fast.next.next # goes up 2 nodes

            if slow == fast: # eventually they will reach the same spot (cycle)
                return True # so we return True

        return False # otherwise no cycle, so we return False