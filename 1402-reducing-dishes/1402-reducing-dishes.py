class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        time = len(satisfaction)
        satisfaction.sort()

        max = 0
        for i in range(time):
            temp = 0
            for i in range(len(satisfaction)):
                temp+=satisfaction[i]*(i+1)
            if max < temp:
                max = temp
            satisfaction.pop(0)
            
        return max