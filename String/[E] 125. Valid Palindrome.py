class Solution:
    def isPalindrome(self, s):
        if s is None:
            return False
        if len(s) <= 1:
            return True
        s = s.lower()
        print(s)
        start = 0 
        end = len(s)-1
        # Consider [0P] !!!! Because alphanumeric
        while start < end:
            if s[start].isalnum() == True and s[end].isalnum() == True:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
                    
            elif s[start].isalnum() == False:
                start += 1
            elif s[end].isalnum() == False:
                end -= 1
        return True


# Runtime: 56 ms, faster than 66.66% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.3 MB, less than 44.05% of Python3 online submissions for Valid Palindrome.