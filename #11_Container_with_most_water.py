class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_v = 0
        i = 0
        j = n-1
        while i< j:
            max_v = max(min(height[j],height[i])*(j-i), max_v)
            if height[j]>height[i]:
                i += 1 
            else:
                j -=1
        return max_v