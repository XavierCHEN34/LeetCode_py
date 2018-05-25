class Solution:
    def isUgly(self, num):
        if num < 1:
            return False
        for factor in [2,3,5]:
            while(num % factor == 0):
                num = num // factor
        return bool(num == 1)
        """
        :type num: int
        :rtype: bool
        """