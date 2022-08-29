class Solution:
    def romanToInt(self, s: str) -> int:
        roman_Dict={"I":1,"V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result=0
        for i in range(len(s)):
            if i==len(s)-1 or roman_Dict[s[i]]>=roman_Dict[s[i+1]]:
                result+=roman_Dict[s[i]]
            else:
                result+=-roman_Dict[s[i]]
        return result