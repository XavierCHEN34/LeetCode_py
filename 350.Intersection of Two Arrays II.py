class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        l1,l2 = sorted(nums1),sorted(nums2)
        n1,n2 = len(l1),len(l2)
        i,j = 0,0

        while( i< n1 and j < n2):
            if l1[i] == l2[j]:
                res.append(l1[i])
                i,j = i+1,j+1
            elif l1[i] > l2[j]:
                j = j+1
            else:
                i = i+1
        return res