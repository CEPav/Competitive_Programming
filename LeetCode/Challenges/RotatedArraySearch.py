
# 36 ms, faster than 100.00% of Python3 online submissions

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Get value at midpoint, compare with start and end to get interval
        """
        
        if target in nums:
            return nums.index(target)
        else:
            return -1
