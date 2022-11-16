class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        expansion = len(columnTitle)-1
        i=0
        sum=0
        while(expansion>=0):
            digit = int((ord(columnTitle[i])-64)*(26**expansion))
            sum += digit
            expansion -= 1
            i += 1
        return sum    