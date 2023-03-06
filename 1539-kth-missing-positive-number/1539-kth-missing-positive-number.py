class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        L = []
        n = len(arr) + k
        for i in range(1, n+1):
            L.append(i)
        LL = [x for x in L if x not in arr]
        return LL[k-1]