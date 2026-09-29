# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = node = ListNode() # combined list for both list1 and list2

        while list1 and list2:
            if list1.val < list2.val: # if 1 < 2
                node.next = list1 # put 1 first since we want it to be in ascending order
                list1 = list1.next # set next element to whatever is next in the list
            else:
                node.next = list2 # if 2 > 1 
                list2 = list2.next # put 2 last since we want it to be in ascending order, and 2 is greater than 1
            node = node.next # set next element to whatever is next in the list
        node.next = list1 or list2 # fill combined list with the rest of the elements from either list that isn't completed yet

        return dummy.next # skip the dummy placeholder, return the actual merged list