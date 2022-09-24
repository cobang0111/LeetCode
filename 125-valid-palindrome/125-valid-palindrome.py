class Solution:
    def isPalindrome(self, s: str) -> bool:
        L=[]

        for i in s.lower():
            if i.isalnum()==True:
                L.append(i)
        
        mid=len(L)//2
        
        if len(L)%2==1:
            L.pop(mid)        
     
        if L[0:mid]==list(reversed(L[mid:])):
            return True
        else:
            return False