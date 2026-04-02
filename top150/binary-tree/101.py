# Definition for a binary tree node.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Using queue
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        q = deque()

        q.append(root.left)
        q.append(root.right)

        while q:
            node1 = q.popleft()
            node2 = q.popleft()

            if node1 is None and node2 is None:
                break

            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            
            q.append(node1.left)
            q.append(node2.right)
            q.append(node1.right)
            q.append(node2.left)

        return True
            
# Using list
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        s_left = []
        s_right = []

        s_left.append(root.left)
        s_right.append(root.right)

        while s_left and s_right:
            node_l = s_left.pop()
            node_r = s_right.pop()

            if node_l is None and node_r is None:
                continue
        
            if node_l is None or node_r is None or node_l.val != node_r.val:
                return False
            
            s_left.append(node_l.left)
            s_right.append(node_r.right)
            s_left.append(node_l.right)
            s_right.append(node_r.left)
        
        return len(s_left) == 0 and len(s_right) == 0
    
# Using recursion
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]):
            if left is None and right is None:
                return True
            
            if left is None or right is None or left.val != right.val:
                return False
            
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        
        return isMirror(root, root)
        





