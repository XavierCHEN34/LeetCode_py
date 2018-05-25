class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        s_reverse = str(x)[::-1]
        if (int(s_reverse) == x):
            return True
        else:
            return False

        """
        :type x: int
        :rtype: bool
        """