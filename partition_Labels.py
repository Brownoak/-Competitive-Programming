class Solution:
    def partitionLabels(self, s: str) -> List[int]:         
        last = {}
        size, end, result = 0, 0, []
        
        for i, letter in enumerate(s):
            last[letter] = i
            
        for start, letter in enumerate(s):
            size +=1
            end = max(end, last[letter])

            if (end == start):
                result.append(size)
                size = 0

        return result