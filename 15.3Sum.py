"""
sorted the array to control the order
then use a hash map to search Two Sum
"""



def three_sum(nums):
    nums = sorted(nums)
    l = []
    # delete repeated
    for i in range(len(nums) - 2 ):
        if i == 0 or nums[i] > nums[i-1]:
            target =  - nums[i]
            buff = {}
            for num in nums[i+1:]:
                if target - num not in buff:
                    buff[num] = 0
                elif buff[target - num] == 0:
                    l.append([-target, num ,target-num ])
                    buff[target - num] = 1
    return l




l = [-1,0,1,2,-1,-4]
print(three_sum(l))






"""
Accepted also
"""


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(num):
        num.sort()
        res = []
        for i in range(len(num)-2):
            #if i == 0 or num[i] > num[i-1]:
                left = i + 1; right = len(num) - 1
                while left < right:
                    if num[left] + num[right] == -num[i]:
                        res.append([num[i], num[left], num[right]])
                        left += 1; right -= 1
                        while left < right and num[left] == num[left-1]: left +=1
                        while left < right and num[right] == num[right+1]: right -= 1
                    elif num[left] + num[right] < -num[i]:
                        while left < right:
                            left += 1
                            if num[left] > num[left-1]: break
                    else:
                        while left < right:
                            right -= 1
                            if num[right] < num[right+1]: break
        return res

