class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount=0
        count=0
        n=len(nums)
        for i in range(n):
            if nums[i]==1:
                count=count+1
                maxcount=max(count,maxcount)
            else:
                count=0    
        return maxcount