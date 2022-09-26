class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        while True:
            x1=nums.pop()
            if nums==[]:
                return x1
                break
            x2=nums.pop()
            if x1!=x2:
                return x1
                break