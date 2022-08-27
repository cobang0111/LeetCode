class Solution:
    def isPalindrome(self, x: int) -> bool:
        check=str(x)
        i=0
        for i in range(len(check)//2):
            if not check[i]==check[len(check)-1-i]:
                return 0
                break
            else:
                i+=1
                continue
        if i==len(check)//2:
            return 1