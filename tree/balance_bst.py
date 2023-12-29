class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_inorder(root, ans=None):
    if not ans:
        ans = []
    if not root:
        return ans
    ans.extend(get_inorder(root.left))
    ans.append(root.data)
    ans.extend(get_inorder(root.right))
    return ans


def build_bst_from_sorted(inorder, start, end):
    if not inorder:
        return None
    if start > end:
        return None
    if start == end:
        return Node(inorder[start])
    mid = (start + end) // 2
    curr = Node(inorder[mid])
    curr.left = build_bst_from_sorted(inorder, start, mid - 1)
    curr.right = build_bst_from_sorted(inorder, mid + 1, end)
    return curr


class Solution:
    def buildBalancedTree(self, root):
        # code here
        inorder = get_inorder(root)
        return build_bst_from_sorted(inorder, 0, len(inorder) - 1)
