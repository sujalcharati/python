#post order Traversal.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    result = []
    if root:
        result.extend(postorderTraversal(root.left))
        result.extend(postorderTraversal(root.right))
        result.append(root.val)
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


print(postorderTraversal(root))
