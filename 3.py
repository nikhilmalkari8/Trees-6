from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalTraversal(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    column_table = defaultdict(list)
    queue = deque([(root, 0, 0)])  # (node, column, depth)

    while queue:
        node, column, depth = queue.popleft()
        if node:
            column_table[column].append((depth, node.val))
            queue.append((node.left, column - 1, depth + 1))
            queue.append((node.right, column + 1, depth + 1))

    # Sort columns by keys
    sorted_columns = sorted(column_table.keys())

    result = []
    for column in sorted_columns:
        # Sort by depth first, then by value
        column_table[column].sort(key=lambda x: (x[0], x[1]))
        result.append([val for _, val in column_table[column]])

    return result
