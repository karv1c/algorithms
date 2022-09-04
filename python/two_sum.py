'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''

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
