class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        curr, max_score = 0, 0
        tokens.sort()
        while tokens:
            if power >= tokens[0]:
                token = tokens[0]
                del tokens[0]
                power -= token
                curr += 1
                max_score = max(max_score, curr)
            elif curr > 0:
                gain = tokens.pop()
                power += gain
                curr -= 1
            else: break
        return max_score