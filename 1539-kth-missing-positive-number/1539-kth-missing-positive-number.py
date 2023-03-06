class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        count = 0
        while True:
            if i not in arr:
                count+=1
            if count == k:
                return i
            i+=1
            