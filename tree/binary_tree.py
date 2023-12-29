from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root):
        self.root = root

    def depth_first_search_preorder_recursive(self):
        answer = []
        if self.root is None:
            return []
        answer.append(self.root.data)
        if self.root.left is not None:
            answer.append(BinaryTree.depth_first_search_preorder_recursive(self.root.left.data))
        if self.root.right is not None:
            answer.append(BinaryTree.depth_first_search_preorder_recursive(self.root.right.data))
        return answer

    def depth_first_search_preorder_nonrecursive(self):
        answer = []
        stack = []
        if self.root is None:
            return []
        curr = self.root
        stack.append(curr)
        while len(stack) > 0:
            curr = stack.pop()
            answer.append(curr.data)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return answer

    def depth_first_postorder_nonrecursive(self):
        answer = []
        stack = []
        if self.root is None:
            return []
        curr = self.root
        stack.append(curr)
        while len(stack) > 0:
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
            curr = stack.pop()
            answer.append(curr.data)
        return answer

    def breadth_first(self):
        answer = []
        q1 = deque()
        q1.append(self.root)
        while len(q1) > 0:
            curr = q1.popleft()
            answer.append(curr.data)
            if curr.left is not None:
                q1.append(curr.left)
            if curr.right is not None:
                q1.append(curr.right)
        return answer
