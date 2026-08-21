class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setm=set(s)
        n=len(setm)
        return n