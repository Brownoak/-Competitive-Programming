class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left =0
        for right, num in enumerate(nums):
            if(num == 0):
                k-=1
            if(k < 0):
                k += (1-nums[left])
                left +=1
        length= right- left +1
        return length