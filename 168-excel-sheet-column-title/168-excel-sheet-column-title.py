class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def mod26(num):
            if num%26==0:
                return 26
            else:
                return num%26
        
        column=''
        

        while columnNumber>26:
            column=chr(mod26(columnNumber)+64)+column
            if mod26(columnNumber)==26:
                columnNumber-=1
            columnNumber=columnNumber//26
    
    
        column=chr(columnNumber+64)+column

        return column