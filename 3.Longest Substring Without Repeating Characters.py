"""
using a sliding window [i,j)

"""
def LS(s):
    max_l = 0
    i = 0
    j = 0
    while(i < len(s) and j <len(s)):
        if s[j] not in s[i:j] :
            j+= 1
            if j-i > max_l:
                max_l = j-i
        else:
            i += 1
    return max_l


s = ''

print(LS(s))