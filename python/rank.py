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
