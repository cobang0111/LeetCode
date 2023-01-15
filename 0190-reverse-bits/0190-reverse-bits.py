class Solution:
    def reverseBits(self, n: int) -> int:
        #int n inputs as decimal
        n=bin(n) #Change to binary string '0bxxxxxx'
        #Fit to 32bit binary number
        add=32-(len(n)-2) 
        reverse_n=''
        for i in range(add):
            reverse_n+='0'
        #Reversing
        for i in range(2,len(n)):
            reverse_n = n[i]+reverse_n
        reverse_n = '0b'+reverse_n #Make binary string
        #Result
        ans=int(reverse_n,2)
        return ans
