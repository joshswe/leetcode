# 8/25/2019 - Joshua Hui

class Solution(object):

    #Sorting
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        
        if len(nums) <= 1:
            return False
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                return True
            i += 1
        return False

# Runtime: 116 ms, faster than 15.99% of Python online submissions for Contains Duplicate.
# Memory Usage: 15.7 MB, less than 96.30% of Python online submissions for Contains Duplicate.

    #Using set
    def containsDuplicate2(self, nums):
        if len(nums) <= 1:
            return False
        emptySet = set()
    
        for element in nums:
            if element in emptySet:
                return True
            else:
                emptySet.add(element)
        return False

# Runtime: 100 ms, faster than 87.92% of Python online submissions for Contains Duplicate.
# Memory Usage: 17.1 MB, less than 75.93% of Python online submissions for Contains Duplicate.