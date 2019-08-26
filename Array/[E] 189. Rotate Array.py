# Joshua Hui - 8/25/2019

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 1:
            return []
        for _ in range(k):
            k = nums.pop()
            nums.insert(0,k)
        
        return nums

# Runtime: 172 ms, faster than 7.48% of Python online submissions for Rotate Array.
# Memory Usage: 12.1 MB, less than 60.42% of Python online submissions for Rotate Array.


# If not in-place:
# But this is wrong if [1,2] ,0
        # lenNums = len(nums)
        # stepsToMove = k % lenNums
        # firstHalf = nums[stepsToMove+1:]
        # secondHalf = nums[:stepsToMove+1]
        # newArray = firstHalf + secondHalf
        # print(newArray)
        # return newArray

# So the correct answer will be
        # lenNums = len(nums)
        # stepsToMove = k % lenNums
        # firstHalf = nums[-stepsToMove:]
        # secondHalf = nums[:-stepsToMove]
        # nums[:] = firstHalf + secondHalf

# Runtime: 44 ms, faster than 86.29% of Python online submissions for Rotate Array.
# Memory Usage: 12.5 MB, less than 10.42% of Python online submissions for Rotate Array.