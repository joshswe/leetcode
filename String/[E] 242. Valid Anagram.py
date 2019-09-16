import collections
class Solution:
    def isAnagram(self, s,t):
        if s is None or t is None:
            return False
        if len(s) != len(t):
            return False
        
        hashTable = collections.defaultdict(int)
        
        for element in s:
            hashTable[element] += 1
        
        for element in t:
            if element not in hashTable:
                return False
            else:
                hashTable[element] -= 1
                if hashTable[element] == 0:
                    hashTable.pop(element)
        return False if hashTable else True


# Runtime: 56 ms, faster than 71.00% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.2 MB, less than 6.25% of Python3 online submissions for Valid Anagram.


    def isAnagram2(self, s,t):
        if s is None or t is None:
            return False
        if len(s) != len(t):
            return False
        
        s =''.join(sorted(s))
        t =''.join(sorted(t))
        pointer = 0
        while pointer <len(s):
            if s[pointer]!=t[pointer]:
                return False
            pointer += 1
        return True

# Runtime: 80 ms, faster than 10.57% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.4 MB, less than 6.25% of Python3 online submissions for Valid Anagram.