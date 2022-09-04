'''Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.'''

class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rtype = []
        sorted = list(arr)
        sorted = list(dict.fromkeys(sorted))
        x = dict()
        sorted.sort()
        arr_dict = {sorted[i]: i for i in range(len(sorted))}
        i = 0
        for i in range(len(arr)):
            rtype.append(arr_dict.get(arr[i])+1)
        return rtype

arr = [40,10,20,30]
print(Solution().arrayRankTransform(arr))
arr = [100,100,100]
print(Solution().arrayRankTransform(arr))
arr = [37,12,28,9,100,56,80,5,12, 0]
print(Solution().arrayRankTransform(arr))
