# Joshua Hui - 8/26/2019

class Solution:


    # Using Del, Count
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 1:
            return []
        
        
        i=0
        numberOfZeroes = 0
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
                numberOfZeroes += 1
            else:
                i+=1
        for _ in range(numberOfZeroes):
            nums.append(0)
        
        return nums

# Runtime: 52 ms, faster than 96.23% of Python3 online submissions for Move Zeroes.
# Memory Usage: 14.8 MB, less than 5.97% of Python3 online submissions for Move Zeroes.

    # In place
    def moveZeroes2(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 1:
            return []

        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        return nums

# Runtime: 56 ms, faster than 84.70% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15.1 MB, less than 5.97% of Python3 online submissions for Move Zeroes.