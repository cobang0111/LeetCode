class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        start = 1
        end = totalTrips * min(time)
        
        while start<end:
            sum_of_time = 0
            mid = (start+end)//2
            for i in time:
                sum_of_time += mid//i
            if sum_of_time >= totalTrips:
                end = mid
            else:
                start = mid+1
        return start   
                    