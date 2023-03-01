class Solution:
    def hammingWeight(self, n: int) -> int:
        new_n=str(bin(n))[2:]
        count=0
        for i in range(len(new_n)):
            if new_n[i]=='1':
                count+=1
        return count