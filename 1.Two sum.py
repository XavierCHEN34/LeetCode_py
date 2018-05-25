"""
O(n**2)
"""

def twoSum(nums, target):
    l = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i!=j:
                l.append(i)
                l.append(j)
                return l
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """


"""
O(n)
the python dict is implemented with Hash map
"""
def twoSum_Hash(nums,target):
    l = []
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in nums:
        if i in buff_dict and buff_dict[ i ] == 0:
                l.append([i,target-i])
                buff_dict[ i ] = 1
        else:
            buff_dict[ target-i ] = 0

    print(buff_dict)
    return l

l = [-4,2,6,4,-2,9]
l2 = [1,1,-1,-1]
print(twoSum_Hash(l,0))


def twoSum_window(nums,target):
    l = []

    n = len(nums)
    nums = sorted(nums)
    i, j  = 0, n-1
    while(i<j):
        if nums[i] + nums[j] == target:
            l.append([nums[i], nums[j]])
            i = i+1
        elif nums[i] + nums[j] < target:
            i = i+1
        elif nums[i] + nums[j] > target:
            j = j-1
    return l

#print(twoSum_window(l2,0))