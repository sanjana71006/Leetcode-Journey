class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        mp={")":"(","}":"{","]":"["} 
        stack=[]
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack or stack[-1]!=mp[ch]:
                    return False
                else:
                    stack.pop()
        return len(stack)==0

