class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) <=1:
            return s
        
        start = 0 
        end = len(s) - 1
        while start<end:
            s[start],s[end] = s[end], s[start]
            start += 1
            end -= 1

# Runtime: 240 ms, faster than 27.92% of Python3 online submissions for Reverse String.
# Memory Usage: 17.7 MB, less than 38.37% of Python3 online submissions for Reverse String.

# Runtime: 228 ms, faster than 81.42% of Python3 online submissions for Reverse String.
# Memory Usage: 17.6 MB, less than 60.46% of Python3 online submissions for Reverse String.