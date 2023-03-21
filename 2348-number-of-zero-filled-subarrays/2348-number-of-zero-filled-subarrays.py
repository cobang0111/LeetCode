class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i=0
        count=0
        continuous = 0
        while i<len(nums):
            if nums[i] == 0:
                continuous+=1
                count+=continuous
            else:
                continuous = 0
            i+=1
        return count