class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #Iterative
        
        if l1 is None or l2 is None:
            return l1 or l2
        dummyNode = ListNode(0)
        dummyNode2 = ListNode(0)
        dummyNode.next = dummyNode2
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                dummyNode2.next = l1
                l1=l1.next
            else:
                dummyNode2.next = l2
                l2=l2.next
            dummyNode2 = dummyNode2.next
        if l1 is None:
            dummyNode2.next = l2
        elif l2 is None:
            dummyNode2.next = l1
        return dummyNode.next.next