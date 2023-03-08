class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        
        while start<end:
            sum_of_hour = 0
            mid = (start + end) // 2
            for i in piles:
                sum_of_hour += math.ceil(i/mid)

            if sum_of_hour > h:
                start = mid + 1
            else :
                end = mid
    
        return start