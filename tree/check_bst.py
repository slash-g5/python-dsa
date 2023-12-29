import sys


def isBST(root):
    def isBSTHelper(tree_root, max_val, min_val):
        if not tree_root:
            return True
        if min_val < tree_root.data < max_val:
            return (isBSTHelper(tree_root.left, tree_root.data, min_val) and
                    isBSTHelper(tree_root.right, max_val, tree_root.data))
        return False
    isBSTHelper(root, sys.maxsize, -sys.maxsize - 1)
