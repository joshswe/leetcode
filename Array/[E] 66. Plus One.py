# Joshua Hui - 8/26/2019

class Solution:
    
    # CONSIDER [9,9,9], [9] 


    # String to Int, Int to String, String List conversion
    def plusOne(self, digits):
        if len(digits) < 1:
            return []
        string = ""
        for element in digits:
            string += str(element)
        integer = int(string)
        integer += 1
        string = str(integer)
        return [int(element) for element in string]

# Runtime: 32 ms, faster than 96.92% of Python3 online submissions for Plus One.
# Memory Usage: 13.8 MB, less than 5.13% of Python3 online submissions for Plus One.