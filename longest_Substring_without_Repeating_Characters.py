class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = 0
        nonRpt = []
        for i in s:
            if i  in nonRpt:
                counter = max(counter , len(nonRpt))
                while nonRpt[0] != i:
                    nonRpt.pop(0)

                nonRpt.pop(0)
                nonRpt.append(i)
        
            else:
                nonRpt.append(i)

        
        return max(counter , len(nonRpt))