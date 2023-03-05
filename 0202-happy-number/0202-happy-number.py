class Solution:
    def isHappy(self, n: int) -> bool:
        temp = n
        L=[]
        while True:
            total = 0
            while True:
                mod = temp % 10
                temp = temp // 10
                total += mod**2
                if temp==0:
                    break
            if total == 1:
                return 1
            elif total in L:
                return 0
            L.append(total)
            temp = total
        
                    
                
            