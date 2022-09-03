class Solution:
    def addBinary(self, a: str, b: str) -> str:
        

        #Make same length
        if len(a)>len(b):
            for i in range(len(a)-len(b)):
                b="0"+b
        elif len(a)<len(b):
            for i in range(len(b)-len(a)):
                a="0"+a   

        L=[]
        #over will be added after one digit
        over="0"
        
        #Calculate each digit by comparing a and b
        for i in range(len(a)-1,-1,-1):
            if a[i]=="1" and b[i]=="1":
                L.append(over)
                over="1"
            elif a[i]=="1" or b[i]=="1":
                if over=="0":
                    L.append("1")
                else:
                    L.append("0")
                    over="1"
            else:
                L.append(over)
                over="0"

        #Last digit processing        
        if over=="1":
            L.append(over)
        
        L.reverse()

        return(''.join(L))
            