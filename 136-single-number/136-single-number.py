class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        while True:
            x1=nums.pop()
            if nums==[]:
                return x1
                break
            
            if x1!=nums.pop():
                return x1
                break