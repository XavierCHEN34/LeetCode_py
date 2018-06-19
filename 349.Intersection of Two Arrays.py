class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = {}
        dic_1 = {}
        for i in nums1:
            dic_1[i] = 0
        for j in nums2:
            if j in dic_1:
                res[j] = 0
        return list( res.keys() )