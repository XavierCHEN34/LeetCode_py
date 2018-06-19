class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ln = len(nums)
        res = set()
        dict = {}
        if ln < 4:
            return []

        nums.sort()
        for  p in range(ln):
            for q in range(p+1, ln):
                if nums[p] + nums[q] not in dict:
                    dict[nums[p] + nums[q]]=[(p, q)]
                else:
                    dict[nums[p] + nums[q]].append((p, q))
        for i in range(ln):
            for j in range(i+1, ln-2):
                T = target - nums[i] - nums[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j:
                            res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [list(i) for i in res]