"""
expend from center == wrong
can only deal with odd palindrome
"""
def longestPalindrome_Center(s):
        l = len(s)
        if l < 2:
            return l
        r = 0
        max_l = 1 + 2*r
        i_max = 0
        r_max = 0

        for i in range(l):
            while(1):
                if i-(r+1) < 0 or i+(r+1) >= l:
                    break
                if s[i-(r+1)] == s[i+(r+1)]:
                    r += 1
                else:
                    break
            if 1+2*r > max_l:
                max_l = 1 + 2 *r
                i_max = i
                r_max = r

        return s[i_max-r_max: i_max+r_max+1]

print(longestPalindrome_Center("sabad"))


"""
Dynamic programming
"""


import numpy as np
def longestPalindrome_DP(s):
    l = len(s)
    p = np.zeros([l,l])
    max_l = 0
    max_i = 0
    max_j = 0

    for j in range(l):
        for i in range(j,-1,-1):
            if( j-i <= 2 and s[i] == s[j]):
                p[i,j] = 1
                if j-i > max_l:
                        max_l = j - i
                        max_i = i
                        max_j = j

            if(j-i>2 and s[i] == s[j] and p[i+1][j-1] == 1):
                p[i,j] = 1
                if j-i > max_l:
                        max_l = j - i
                        max_i = i
                        max_j = j

    return(s[max_i:max_j+1])

print(longestPalindrome_DP("sabad"))