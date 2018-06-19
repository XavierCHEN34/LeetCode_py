
class Solution(object):
    def minSubArrayLen(self, s, nums):
        right, sum = 0, 0
        res = s+1
        for left in range(len(nums)):
            while right < len(nums) and sum < s:
                sum += nums[right]
                right += 1
            if sum >= s:
                res = min(res, right - left)
            sum -= nums[left]    
        if res == s+1:
            return 0
        return res