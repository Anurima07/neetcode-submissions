class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        maxhig=0
        for i in range(n):
            for j in range(i+1,n):
                hig=(j-i)*min(heights[i],heights[j])
                maxhig=max(hig,maxhig)  
        return maxhig        