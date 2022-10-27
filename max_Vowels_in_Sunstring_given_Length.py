class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        best=count=0
        vowel= "aeiou"
        for i, x in enumerate(s):
            if x in vowel:
                count+= 1
            if i >= k and s[i-k] in vowel:
                count-= 1
            best = max(best, count)
            
        return best