class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


class Tree:
    def __init__(self, root):
        self.root = root



    def breadth_first_search(self):
        answer = []
