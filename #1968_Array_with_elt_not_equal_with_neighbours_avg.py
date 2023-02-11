class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1 , len(nums)-1):
            a = nums[i-1]> nums[i] and nums[i]> nums[i+1]
            b = nums[i-1]<nums[i] and nums[i]<nums[i+1]
            
            if  a or b:
                nums[i],nums[i+1] = nums[i+1],nums[i]
        return nums