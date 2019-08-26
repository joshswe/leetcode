class Solution:

    # Dictionary
    def singleNumber(self, nums):
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0] # without [0] it will return (key,value) but we only want the key, so need to add [0]

# Runtime: 108 ms, faster than 25.96% of Python3 online submissions for Single Number.
# Memory Usage: 16.3 MB, less than 6.56% of Python3 online submissions for Single Number.

# Time complexity : O(n * 1) = O(n)O(n⋅1)=O(n). Time complexity of for loop is O(n)O(n). Time complexity of hash table(dictionary in python) operation pop is O(1)O(1).

# Space complexity : O(n)O(n). The space required by hash_table is equal to the number of elements in nums. 


    # Bit Manipulation
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a

# Time complexity : O(n)O(n). We only iterate through nums, so the time complexity is the number of elements in nums.

# Space complexity : O(1)O(1).




# Runtime: 96 ms, faster than 87.62% of Python3 online submissions for Single Number.
# Memory Usage: 16.4 MB, less than 6.56% of Python3 online submissions for Single Number.