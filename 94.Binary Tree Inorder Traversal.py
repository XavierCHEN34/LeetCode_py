class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self. recursive_inorder (root, res)
        print(res)
        return res
    def recursive_inorder(self, root, res):#递归中序遍历
        if root:
            self.recursive_inorder(root.left, res)
            res.append(root.val)
            self.recursive_inorder(root.right, res)