def Closet(nums,target):
    min_v = 999
    min_com = None

    nums = sorted(nums)
    for i in range(len(nums) -2):
        left = i+1
        right = len(nums) - 1
        while(left < right):
            sum_3 = nums[i] + nums[left] + nums[right]
            #print(i,left,right,sum_3)
            if sum_3 == target:
                return 0
            elif abs(sum_3 - target) < min_v:
                min_v = abs( sum_3 -target )
                min_com = sum_3

            if sum_3 < target:
                left += 1
            if sum_3 > target:
                right -= 1
    return min_com

l = [-4, -1, 1, 2]
l2 = [0,1,2]
print( Closet(l2,1))

