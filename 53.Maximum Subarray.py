"""
DP each element represents the max value of substing [:i] ===> [::]
"""

def maxSubArray(nums):
        l = [nums[0]]
        for i in range(1,len(nums)):
            if l[i-1] > 0:
                l.append(l[i-1] + nums[i])
            else:
                l.append(nums[i])
        print(l)
        return max(l)

ma = [-2,1,-3,4,-1,2,1,-5,4]
ma2 = [-2,1]
print(maxSubArray(ma2))

