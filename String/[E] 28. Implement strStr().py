class Solution:

    # Sliding window
    def strStr(self, haystack,needle):
        # What should we return when needle is an empty string? This is a great question to ask during an interview.
        
        if len(needle) < 1:
            return 0
        
        windowFront = 0   
        
        windowBack = len(needle)-1
        
        while windowBack < len(haystack):
            if haystack[windowFront:windowBack+1] == needle:
                return windowFront
            windowFront += 1
            windowBack += 1     
               
        return -1

# Runtime: 32 ms, faster than 94.08% of Python3 online submissions for Implement strStr().
# Memory Usage: 14 MB, less than 12.31% of Python3 online submissions for Implement strStr().