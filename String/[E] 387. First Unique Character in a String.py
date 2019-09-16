import collections 

class Solution:

    # Use hashtable only
    def firstUniqChar(self, s):
        if len(s) < 1:
            return -1
        if len(s) == 1:
            return 0
        
        hashTable = collections.defaultdict(list)
        position = len(s)
        
        for i, element in enumerate(s):
            hashTable[element].append(i)
        for element in hashTable:
            if len(hashTable[element]) == 1:
                position = min(position,hashTable[element][0])
        
        return position if position != len(s) else -1



# Runtime: 140 ms, faster than 35.58% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 15.1 MB, less than 6.52% of Python3 online submissions for First Unique Character in a String.


    # Use counter
    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1