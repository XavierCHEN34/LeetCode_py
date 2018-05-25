class Solution:
    def searchMatrix(self,L, target):
        
        m = len(L)
        if m == 0:
            return False
        n = len(L[0])
        if n == 0:
            return False
        row_index, col_index = 0,0
        if target < L[0][0]:
            return False

        for i in range(len(L)):
            if  L[i][-1] < target:
                row_index += 1
        if row_index == len(L):
            return False
       
        for i in L[row_index]:
            if i == target:
                return True
        return False

        
        
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        