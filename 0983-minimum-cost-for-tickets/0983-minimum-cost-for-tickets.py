class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel_cal = []
        total_charge = []


        for i in range(1, days[-1]+1):
            total_charge.append(0)
            if i in days:
                travel_cal.append(1)
            else:
                travel_cal.append(0)

        i=0

        if travel_cal[0] == 0:
            total_charge[0] = 0
            i+=1

        while i < len(travel_cal):
            if travel_cal[i] != 1:
                total_charge[i] = total_charge[i-1]
            else:
                if i >= 30:
                    total_charge[i]+=min(total_charge[i-1]+costs[0], total_charge[i-7]+costs[1], total_charge[i-30]+costs[2])
                elif i >= 7:
                    total_charge[i]+=min(total_charge[i-1]+costs[0], total_charge[i-7]+costs[1], costs[2])
                else:
                    total_charge[i]+=min(total_charge[i-1]+costs[0], costs[1], costs[2])

            i+=1


        return total_charge[-1]   

                
        