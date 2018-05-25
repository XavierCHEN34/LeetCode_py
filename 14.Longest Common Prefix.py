"""
use function 'zip' to simplify the code
"""


def longestCommonPrefix( strs):
        number = 0
        for i in list(zip(*strs)):
            if len(set(i)) == 1:
                number = number +1
            else:
                break
        if number == 0:
            return ''
        return strs[0][:number]

print(longestCommonPrefix(  []   ))