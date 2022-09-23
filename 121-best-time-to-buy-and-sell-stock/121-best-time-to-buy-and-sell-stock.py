class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy=prices[0]
        gap=0
        
        for i in prices[1:]:
            if i<buy:
                buy=i
            elif i-buy>gap:
                gap=i-buy

        
        if gap>0:
            return gap
        else:
            return 0

