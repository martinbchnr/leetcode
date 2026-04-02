from collections import Optional, List, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # handles case of no tree at all
        if root is None:
            return [0.0]
        
        average_val = [float(root.val)]
        # handle case of single node
        if root.left is None and root.right is None:
            return average_val
        
        
        depth = 1
        # handle actual tree
        unexplored = deque()

        unexplored.append((root.left, depth + 1))
        unexplored.append((root.right, depth + 1))
        
        depth_avg = []
        while unexplored:
            node = unexplored.popleft()
            if node is not None:
                depth_avg.append(node.val)
            
            

            if len(unexplored) == 0:
                unexplored


        

        
        
