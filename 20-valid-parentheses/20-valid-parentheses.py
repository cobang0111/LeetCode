class Solution:
    def isValid(self, s: str) -> bool:
        # Make List for checking status of Open/Close
        L=[]

        # If length of s is odd, it is invalid
        if len(s)%2==1:
            return False

        # add list if value is 
        for i in s:
            if len(L)>0:
                # Case of close Bracket
                if i in [")","}","]"]:
                    # If Last element of L be closed by i, remove it from L
                    if L[-1]=="(" and i==")":
                        L.pop()
                    #ASCII Code difference between open bracket and close bracket is 2 except "(" and ")"
                    elif ord(i)-2==ord(L[-1]):
                        L.pop()
                    #If there is no element for close, it is invalid
                    else:
                        return False
                # Case of open Bracket
                else:
                    L.append(i)
            # If nothing in list L, bring new one 
            else:
                L.append(i)

        # For valid, L must be empty 
        if len(L)==0:
            return True
        else:
            return False