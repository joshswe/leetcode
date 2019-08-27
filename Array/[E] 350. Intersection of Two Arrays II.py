# Joshua Hui - 8/26/2019

import collections
class Solution:

    # Hashtable
    def intersect(self, nums1, nums2):
        if len(nums1) == 0 or len(nums2)==0:
            return []
        result = []
        
        hashTable = collections.defaultdict(int)
        for element in nums1:
            hashTable[element] += 1
        
        for element2 in nums2:
            if element2 in hashTable and hashTable[element2] >0:
                result.append(element2)
                hashTable[element2]-=1
        return result
    
# Runtime: 52 ms, faster than 91.49% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 13.9 MB, less than 5.72% of Python3 online submissions for Intersection of Two Arrays II.


    # Two Pointer

    def intersect2(self, nums1, nums2):
        if len(nums1) == 0 or len(nums2)==0:
            return []
        result = []
        nums1.sort()
        nums2.sort()

        i = 0
        j = 0
        
        while i<len(nums1) and j < len(nums2):
            if (nums1[i]==nums2[j]):
                result.append(nums1[i])
                i+=1
                j+=1
            elif (nums1[i]>nums2[j]):
                j+=1
            elif (nums2[j]>nums1[i]):
                i+=1
        return result
# Runtime: 52 ms, faster than 91.49% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 14 MB, less than 5.72% of Python3 online submissions for Intersection of Two Arrays II.