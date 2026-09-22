# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = node = ListNode() # combine the two lists into a new list that is initially empty

        while list1 and list2: # while both are non-empty
            if list1.val < list2.val: 
                node.next = list1 # set next element to be list1
                list1 = list1.next 
            else:
                node.next = list2 # set next element to be list2
                list2 = list2.next
            node = node.next # move onto the next element
        node.next = list1 or list2 # fill rest of dummy list with either list1 or list2 whichever isnt empty yet

        return dummy.next # skip the dummy placeholder, return the actual merged list