class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        p = res= 0
        for i in range(0, k-1):
            p += arr[i]
        for i in range(k-1, len(arr)):
            p += arr[i]
            if p >= (threshold * k):
                res+= 1
            p-= arr[i- k + 1]
        return res