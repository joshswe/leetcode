# Recursion

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        
        return self.maxDepthHelper(root)
    
    def maxDepthHelper(self,currentNode):
        if currentNode is None:
            return 0
        
        leftDepth = self.maxDepthHelper(currentNode.left)
        rightDepth = self.maxDepthHelper(currentNode.right)
        
        return max(leftDepth,rightDepth)+1


# Runtime: 44 ms, faster than 93.24% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16 MB, less than 12.50% of Python3 online submissions for Maximum Depth of Binary Tree.