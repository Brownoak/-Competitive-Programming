class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum= sum(nums)
        left=0

        right= totalSum -left
        
        for i in range (len(nums)):
            right-= nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1