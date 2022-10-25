class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left=right=1
        for i in (nums):
            output.append(left)
            left = left * i
        for i in range(len(nums)-1, -1, -1):
            output[i]= right*output[i]
            right = right* nums[i]
        return output