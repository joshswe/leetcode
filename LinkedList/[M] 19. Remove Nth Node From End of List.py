class Solution:
    def removeNthFromEnd(self, head, n):
        
        if head is None:
            return None
        
        firstNode = head
        secondNode = head
        previousNode = None
                
        for _ in range(n-1):
            secondNode = secondNode.next
            if secondNode == None:
                return None
        
        if secondNode.next is None:
            head = head.next
            return head
            
        else:
            while secondNode.next:
                previousNode = firstNode
                firstNode = firstNode.next
                secondNode = secondNode.next
                
        
            previousNode.next = firstNode.next
            return head