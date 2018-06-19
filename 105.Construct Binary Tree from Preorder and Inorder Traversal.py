class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None



class Solution(object):
    def helper(self,inorder):
        if not self.preorder or not inorder:
            return None
        root = TreeNode(self.preorder[0])

        self.preorder=self.preorder[1:]

        root.left = self.helper(inorder[:inorder.index(root.val)])
        root.right = self.helper(inorder[inorder.index(root.val)+1:])
        return root

    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        return self.helper(inorder)
