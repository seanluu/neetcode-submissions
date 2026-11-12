# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = node = ListNode() # create an empty list for us to add or summed both lists to (eventually)

        carry = 0 # keep track of extra tens for the next sum

        while l1 or l2 or carry: # continue til all digits and carry are processed

            # if a list is shorter than the other, treat missing digits as 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry # calculate total sum for our val

            carry = val // 10 # gives carry for the next pos (tens digit)
            val = val % 10 # gives digit to store in this node (ones digit)

            node.next = ListNode(val) # connect new digit to sum list

            node = node.next # move pointer forward in our summed list 

            # move l1 forward if exists
            l1 = l1.next if l1 else None
            # move l2 forward if exists
            l2 = l2.next if l2 else None

        return dummy.next # return head of new LL