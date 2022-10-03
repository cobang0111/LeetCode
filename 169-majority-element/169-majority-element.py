class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        number=nums[0]

        for i in nums:
            if number==i:
                count+=1
            else:
                number=i
                count=1
    
            if count>(len(nums)/2):
                break
        
        return number