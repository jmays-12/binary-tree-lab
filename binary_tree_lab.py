from re import L
from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    l = max_depth(root.left)
    r = max_depth(root.right)

    return (max(l, r)) + 1


# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
        return None
    if root.val > p.val and root.val > q.val:
        return lowest_common_ancestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:  
        return lowest_common_ancestor(root.right, p, q)
    else:
        return root