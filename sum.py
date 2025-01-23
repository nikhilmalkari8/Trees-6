class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    if not root:
        return 0

    # If the node's value is in range, include it and explore both children
    if low <= root.val <= high:
        return root.val + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high)
    # If the node's value is less than low, skip the left subtree
    elif root.val < low:
        return rangeSumBST(root.right, low, high)
    # If the node's value is greater than high, skip the right subtree
    else:
        return rangeSumBST(root.left, low, high)
