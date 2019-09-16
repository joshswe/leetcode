class Solution(object):
    def isValidBST(self, root):
        if root is None:
            return True
        
        
        return self.isValidBSTHelper(-float('inf'),root,float('inf'))
    
    def isValidBSTHelper(self,minValue,currentNode,maxValue):
        if currentNode is None:
            return True
        if currentNode.val >= maxValue or currentNode.val <= minValue:
            return False
        
        return self.isValidBSTHelper(minValue,currentNode.left,currentNode.val) and self.isValidBSTHelper(currentNode.val,currentNode.right,maxValue)


# Runtime: 32 ms, faster than 81.10% of Python online submissions for Validate Binary Search Tree.
# Memory Usage: 16.5 MB, less than 56.60% of Python online submissions for Validate Binary Search Tree.