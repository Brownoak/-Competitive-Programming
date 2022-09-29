class Solution:
    def isValid(self, s: str) -> bool:
        dictionary= {"]":"[", ")":"(", "}":"{"}
        stack = []
        
        for i in s:
            if i in dictionary:
                if not stack or dictionary[i] != stack[-1] :
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
                
        return  stack == []