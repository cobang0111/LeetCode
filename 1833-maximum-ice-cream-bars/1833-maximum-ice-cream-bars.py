class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        i=0
        costs.sort()
        for x in costs:
            if coins>=x:
                coins-=x
                i+=1
            else:
                break
        return i