class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        i=0
        for i in range(len(nums)):
            j=i+1
            while j<len(nums):
                if target-nums[i]==nums[j]:
                    result.append(i)
                    result.append(j)
                    return result
                    break
                else:
                    j+=1
            i+=1
                