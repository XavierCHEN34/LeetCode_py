# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        stack,res = [(root, root.val)], 0
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    if value == sum:
                        return True
                if node.right:
                    stack.append((node.right, value+node.right.val))
                if node.left:
                    stack.append((node.left, value+node.left.val))

        return False
