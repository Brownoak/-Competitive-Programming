class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            temp=0
            for j in range(len(nums)):
                if nums[j] < i:
                    temp+=1
            ans.append(temp)
            
        return ans