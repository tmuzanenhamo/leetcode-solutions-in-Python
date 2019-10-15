
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        x = len(nums)
        for m  in range(i,x,1):
             for k in range(m+1,x,1):
                 l = nums[m]+ nums[k]
                 if l == target:
                        return [m,k]        


