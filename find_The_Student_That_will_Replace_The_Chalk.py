class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k=k%sum(chalk)
        presum=0
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]