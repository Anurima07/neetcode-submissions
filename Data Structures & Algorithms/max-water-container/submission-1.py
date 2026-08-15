class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        maxhig=0
        l=0
        r=n-1
        while l<r:
            hig=(r-l)*min(heights[l],heights[r])
            maxhig=max(hig,maxhig)  
            if  heights[l]< heights[r]:
                l+=1
            else:
                 r-=1   
        return maxhig        