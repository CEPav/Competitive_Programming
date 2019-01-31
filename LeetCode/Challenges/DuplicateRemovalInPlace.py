#In place duplicate removal

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for numb in nums:
            while nums.count(numb) > 1:
                nums.remove(numb)
        return len(nums)
        
#Faster
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) <= 1:
            return len(nums)
        else:
            Previous = 0
            for i in range(1,len(nums)):
                if nums[i] != nums[Previous]:
                    Previous += 1
                    nums[Previous] = nums[i]
                    
            return Previous+1
