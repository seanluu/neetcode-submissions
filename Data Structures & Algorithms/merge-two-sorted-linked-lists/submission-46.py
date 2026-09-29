# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = node = ListNode() # dummy stays fixed as anchor; node walks forward to build the list

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1 # list1's current value is smaller — attach it next
                list1 = list1.next
            else:
                node.next = list2 # list2's value is smaller or equal — attach it next
                list2 = list2.next
            node = node.next # advance node forward to keep building the merged list
        node.next = list1 or list2 # splice in whichever list still has remaining nodes

        return dummy.next # skip the dummy placeholder, return the actual merged list