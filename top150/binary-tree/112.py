# Definition for a binary tree node.
from collections import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        if root.val == targetSum and root.left is None and root.right is None:
            return True
        
        unexplored = deque()

        unexplored.append((root.left, root.val))
        unexplored.append((root.right, root.val))
        
        while unexplored:
            curr_node, prev_cost = unexplored.popleft()
            if curr_node is None:
                continue
            if prev_cost + curr_node.val == targetSum:
                if curr_node.left is None and curr_node.right is None:
                    return True
            
            unexplored.appendleft((curr_node.left, prev_cost + curr_node.val))
            unexplored.appendleft((curr_node.right, prev_cost + curr_node.val))

        return False





