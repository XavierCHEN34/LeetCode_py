class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        di = {"(":0, "[":1,"{":2 }
        do = {")":0, "]":1,"}":2 }
        for i in s:
            if i in di:
                stack.append(di[i])
            else:
                if len(stack)==0:
                    return False
                if do[i] != stack.pop():
                    return False
        if len(stack) == 0:
            return True
        else:
            return False