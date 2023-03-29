class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        time = len(satisfaction)
        satisfaction.sort()
        max_dish = 0
        temp = 0
        for i in range(time):
            temp += sum(satisfaction[-i-1:])
            if temp > max_dish:
                max_dish = temp
            
        return max_dish