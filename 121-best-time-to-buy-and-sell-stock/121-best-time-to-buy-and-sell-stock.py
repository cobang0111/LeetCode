class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy=prices[0]
        sell=0
        gap=0
        
        for i in prices[1:]:
            if i<buy:
                buy=i
            elif i-buy>gap:
                sell=i
                gap=sell-buy

        
        if gap>0:
            return gap
        else:
            return 0

