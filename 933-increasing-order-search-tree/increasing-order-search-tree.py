# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []

        def inOrder(node):
            if not node:
                return None
            inOrder(node.left)
            values.append(node.val)
            inOrder(node.right)
        inOrder(root)

        dummy  = TreeNode()
        current  = dummy

        for val in values:
            current.right = TreeNode(val)
            current = current.right
        return dummy.right

        