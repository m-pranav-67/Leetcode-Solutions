class Solution(object):
    def maxProfit(self, prices):
        maxp=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                prof = prices[j]-prices[i]
                maxp = max(maxp,prof)
        return maxp
      
        