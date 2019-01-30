
# Not very good solution

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        moves = 0
        while moves <= zeros:
            moves += 1
            for i,val in enumerate(nums):
                if val == 0:
                    nums.pop(i)
                    nums.append(0)

# Better

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        return nums.sort(key=lambda x:1 if x!=0 else 0,reverse=True)
