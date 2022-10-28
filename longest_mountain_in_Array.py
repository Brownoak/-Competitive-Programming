class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longest= left = right= 0

        for i in range(1, len(arr)- 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                left = right = i
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                while right < len(arr)- 1 and arr[right + 1] < arr[right]:
                    right += 1
                longest = max(longest, (right - left + 1))
        return longest