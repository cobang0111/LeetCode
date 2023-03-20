class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possible = 0
        i = 0
        while i<len(flowerbed):
            if flowerbed[i] == 1 :
                i+=2
            elif i+1 < len(flowerbed) and flowerbed[i+1] == 1:
                i+=3
            else :
                i+=2
                possible+=1
            
        if possible >= n:
            return 1
        else : 
            return 0
        
        