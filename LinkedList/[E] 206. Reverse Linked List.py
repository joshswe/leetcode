class Solution(object):
    def reverseList(self, head):
        # if head is None:
        #     return None
        # elif head.next is None:
        #     return head
        # else:
        #     p = self.reverseList(head.next)
        #     head.next.next = head
        #     head.next = None
        #     print(p.val)
        #     return p

        if head is None:
            return None
        if head.next is None:
            return head
        currentNode = head
        previousNode = None
        nextNode = None
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        
        return previousNode
# Runtime: 20 ms, faster than 84.59% of Python online submissions for Reverse Linked List.
# Memory Usage: 13.6 MB, less than 57.41% of Python online submissions for Reverse Linked List.