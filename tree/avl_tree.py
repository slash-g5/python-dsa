def print_binary_tree(root):
    if root is None:
        return

    queue = [root]

    while queue:
        level_size = len(queue)
        level_values = []

        for i in range(level_size):
            node = queue.pop(0)
            if node:
                level_values.append(str(node.data))
                queue.append(node.left)
                queue.append(node.right)
            else:
                level_values.append("null")

        if all(value == "null" for value in level_values):
            break

        print(" ".join(level_values))
        

def binary_search_insert(node, data, height):
    if node is None:
        return AvlTreeNode(data)
    if data >= node.data:
        node.right = binary_search_insert(node.right, data, height+1)
    else:
        node.left = binary_search_insert(node.left, data, height + 1)
    return node


class AvlTreeNode:
    def __init__(self, data, left, right, height):
        self.data = data
        self.left = left
        self.right = right
        self.height = height


class AvlTree:
    def __init__(self, root):
        self.root = root
    
    def insert(self, data):
        if data is None:
            return
        self.root = binary_search_insert(self.root, data, 0)
        self.rebalance()

    def rebalance(self):
        pass
    