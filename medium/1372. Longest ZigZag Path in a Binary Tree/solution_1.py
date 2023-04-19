# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> List[int]:
            if not node:
                return -1, -1, -1
            left_subtree = dfs(node.left)
            right_subtree = dfs(node.right)
            return (left_subtree[1] + 1, 
                    right_subtree[0] + 1, 
                    max(left_subtree[1] + 1, right_subtree[0] + 1, left_subtree[2], right_subtree[2]))
        return dfs(root)[2]