class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        size = len(nums)-1
        tmp = 0

        while tmp<size:
            mid = (tmp+size)//2
            if nums[mid]<target:
                tmp = mid+1
            else:
                size = mid

        if nums[tmp]<target:
            return tmp+1
        return tmp