from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the node is None, we've hit a leaf's child
        if not root:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively call the function on the children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # this will anyways be called at the end because the root node itself is not getting mirrored
        return root