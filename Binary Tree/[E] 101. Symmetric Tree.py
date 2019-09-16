class Solution:

    def isSymmetric(self, root: TreeNode):
        if root is None:
            return True

        return self.isSymmetricHelper(root,root)

    def isSymmetricHelper(self,leftSubtreeNode,rightSubtreeNode):
        if leftSubtreeNode is None and rightSubtreeNode is None:
            return True
        if leftSubtreeNode is None or rightSubtreeNode is None:
            return False
        if leftSubtreeNode.val != rightSubtreeNode.val:
            return False
        return self.isSymmetricHelper(leftSubtreeNode.left,rightSubtreeNode.right) and self.isSymmetricHelper(leftSubtreeNode.right,rightSubtreeNode.left)

# Runtime: 40 ms, faster than 75.13% of Python3 online submissions for Symmetric Tree.
# Memory Usage: 13.9 MB, less than 5.17% of Python3 online submissions for Symmetric Tree.
