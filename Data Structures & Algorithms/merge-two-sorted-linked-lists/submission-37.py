class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = node = ListNode() # use a dummy node, aka create an empty LL

        while list1 and list2: # while list1 and list2 actually have elements still
            if list1.val < list2.val: # go by whichever value is lower, to keep the merged list sorted
                node.next = list1 # set next element of new list to be list1
                list1 = list1.next # set next element of list1 to be the one that follows after it
            else:
                node.next = list2 # set next element of new list to be list2
                list2 = list2.next # set next element of list2 to be the one that follows after it
            node = node.next # set next element of the node to be the one after it
        node.next = list1 or list2 # fill rest of the LL we created with either list1 or list2
        # (whichever one isn't depleted yet)

        return dummy.next # return final new LL that we created earlier

        # time complexity: O(n + m)
        # we iterate through list1 and list2 exactly once combined,
        # consuming one node per iteration from either list

        # space complexity: O(1)
        # we reuse the existing nodes from list1/list2, no new nodes are allocated