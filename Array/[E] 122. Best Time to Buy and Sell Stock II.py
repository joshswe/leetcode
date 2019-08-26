# Joshua Hui - 8/25/2019


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        total = 0
        i = 1
        while (i<len(prices)):
            if prices[i]>prices[i-1]:
                total += prices[i]-prices[i-1]
            i+=1
        
        return total
#Runtime: 44 ms, faster than 82.45% of Python online submissions for Best Time to Buy and Sell Stock II.
#Memory Usage: 12.5 MB, less than 95.35% of Python online submissions for Best Time to Buy and Sell Stock II.