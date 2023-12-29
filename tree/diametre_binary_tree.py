# User function Template for python3
# https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1?page=4&sortBy=submissions

def diameterHelper(root):
    if root is None:
        return 0, 0, 0
    left_d, left_h, left_o = diameterHelper(root.left)
    right_d, right_h, right_o = diameterHelper(root.right)
    inc_root = left_h + right_h + 1
    return inc_root, max(left_h, right_h) + 1, max(left_o, max(right_o, inc_root))


class Solution:

    # Function to return the diameter of a Binary Tree.

    def diameter(self, root):
        return diameterHelper(root)[2]
