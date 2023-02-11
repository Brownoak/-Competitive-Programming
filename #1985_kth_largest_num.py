class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        result = []
        for i in nums:
            result.append(int(i))
        result.sort()
        return str(result[-k])