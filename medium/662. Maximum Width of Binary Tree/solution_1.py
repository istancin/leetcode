from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 0)])
        max_width = 0

        while queue:
            level_len = len(queue)
            _, start_left = queue[0]

            for i in range(level_len):
                node, idx = queue.popleft()
                if node.left:
                    queue.append((node.left, idx*2+1))
                if node.right:
                    queue.append((node.right, idx*2+2))
            
            max_width = max(max_width, idx - start_left + 1)
        
        return max_width