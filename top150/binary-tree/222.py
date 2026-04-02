# Definition for a binary tree node.
from collections import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# this solution requires O(n) time and O(n) space, but there is a solution that requires O(log(n)) time and O(1) space
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        unexplored = deque()

        unexplored.append((root.left, 1))
        unexplored.append((root.right, 1))

        count = 1

        while unexplored:
            curr_node, prev_depth = unexplored.popleft()
            if curr_node is None:
                return count
            count += 1

            unexplored.append((curr_node.left, prev_depth + 1))
            unexplored.appned((curr_node.right, prev_depth + 1))

        return count

        
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_depth = 0
        right_depth = 0

        left_node = root
        right_node = root

        while left_node is not None:
            left_depth += 1
            left_node = left_node.left
        
        while right_node is not None:
            right_depth += 1
            right_node = right_node.right
        
        if left_depth == right_depth:
            return (2 ** left_depth) - 1
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1