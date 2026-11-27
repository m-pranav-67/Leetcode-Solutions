class Solution(object):
    def maxProfit(self, prices):
        minp=float('inf')
        maxp=0
        for p in prices:
            minp=min(minp,p)
            prof=p-minp
            maxp=max(maxp,prof)
        return maxp
      
        