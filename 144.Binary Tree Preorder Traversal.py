class Solution(object):

    def preorder(self,root,l):
        if root:
            l.append(root.val)
            self.preorder(root.left,l)
            self.preorder(root.right,l)
        return l


    def preorderTraversal(self, root):
        l = []
        self.preorder(root,l)
        return l


        """
        :type root: TreeNode
        :rtype: List[int]
        """