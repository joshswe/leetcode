# Joshua Hui - 8/26/2019

import collections
class Solution:
    def twoSum(self, nums,target):

        # If there is only one number 
        if len(nums) <2:
            return False
        
        hashTable = collections.defaultdict(list)
        
        for i,element in enumerate(nums):
            remain = target - element
            if remain not in hashTable:
                hashTable[element].append(i)
            else:
                return [hashTable[remain][0],i]

# Runtime: 56 ms, faster than 87.25% of Python3 online submissions for Two Sum.
# Memory Usage: 15.8 MB, less than 5.11% of Python3 online submissions for Two Sum.