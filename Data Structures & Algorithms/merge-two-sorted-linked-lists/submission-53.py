# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = node = ListNode() # dummy is a placeholder before the real head, node is the tail we build from

        while list1 and list2: # both still have nodes to compare
            if list1.val < list2.val:
                node.next = list1 # attach the smaller node to the tail
                list1 = list1.next # move list1 forward
            else:
                node.next = list2 # attach the smaller node to the tail
                list2 = list2.next # move list2 forward
            node = node.next # tail moves onto the node we just attached

        node.next = list1 or list2 # attach whatever's left (already sorted), or None if both are done

        return dummy.next # skip the dummy, the real merged list starts after it

        # tc: O(n + m), each node is visited once
        # sc: O(1), we relink existing nodes, no new ones besides the dummy