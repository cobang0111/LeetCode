class Solution:
    def climbStairs(self, n: int) -> int:
        
        second_Before=0
        first_Before=1

        for i in range(n):
            k=second_Before+first_Before
            second_Before=first_Before
            first_Before=k
        
        return k
            