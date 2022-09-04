class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        out = dict()
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in out.keys():
                return [i,out.get(sub)]
            else:
                out[nums[i]] = i
        return None

nums = [2,7,11,13]
target = 9
print(Solution().twoSum(nums, target))