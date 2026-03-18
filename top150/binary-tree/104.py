from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def eval_recursive(node: Optional[TreeNode], counter: int) -> int:
    if node == None:
        return counter
    if node.left is not None or node.right is not None:
        counter += 1
        return max(eval_recursive(node.left, counter), eval_recursive(node.right, counter))
    else:
        return counter

def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return eval_recursive(root, 1)

TreeNode(15)
