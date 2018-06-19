class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        depth = 0
        q = [root]
        while len(q) != 0:
            depth += 1
            for i in range(0, len(q)):

                if q[0].left == None and q[0].right == None:
                    return depth

                if q[0].left:
                    q.append(q[0].left)

                if q[0].right:
                    q.append(q[0].right)

                del q[0]
        return depth