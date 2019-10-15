
class Solution:
    def twoSum(self, nums, target):
        i = 0
        j = 1
        x = len(nums)
        for m  in range(i,x,1):
             for k in range(m+1,x,1):
                 l = nums[m]+ nums[k]
                 if l == target:
                     print([m,k])


        

def main():
    List = [2,5,5,11]
    d = Solution()
    d.twoSum(List,10)

if __name__ == "__main__":
    main()


