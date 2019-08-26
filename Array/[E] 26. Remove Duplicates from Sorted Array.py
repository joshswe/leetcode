# Joshua Hui - 8/25/2019


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0
        
        if len(nums) == 1:
            return 1
        
        i = 1
        
        while i<len(nums):
            if nums[i]==nums[i-1]:
                del nums[i] # This will be faster than nums.pop(i)
            else:
                i+=1
        return len(nums)
# pop
#Runtime: 88 ms, faster than 17.16% of Python online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 13.8 MB, less than 6.25% of Python online submissions for Remove Duplicates from Sorted Array.
# del
#Runtime: 80 ms, faster than 32.14% of Python online submissions for Remove Duplicates from Sorted Array.
#Memory Usage: 13.6 MB, less than 64.06% of Python online submissions for Remove Duplicates from Sorted Array.