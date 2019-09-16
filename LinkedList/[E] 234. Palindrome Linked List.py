# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        
        slow, fast = head,head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next 
        
        newHead = self.reverse(slow)
        
        while newHead is not None and head is not None:
            if (newHead.val != head.val):
                break
            newHead = newHead.next
            head = head.next
        
        if newHead is None or head is None:
            return True
    
        return False
    
    def reverse(self,head):
        previousNode = None
        nextNode = None
        currentNode = head
        
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        return previousNode


#