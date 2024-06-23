

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    result = []
    if root:
        result = inorder_traversal(root.left)
        result.append(root.val)
        result += inorder_traversal(root.right)
    return result



node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, left=node4, right=node5)
node3 = TreeNode(3)
node1 = TreeNode(1, left=node2, right=node3)
print("Inorder traversal:", inorder_traversal(node1))