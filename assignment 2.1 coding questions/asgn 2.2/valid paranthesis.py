# Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashmap={')':'(',   '}':'{',   ']':'['}
        for x in s:
            if stack and (x in hashmap and stack[-1]== hashmap[x]):
                stack.pop()
            else:
                stack.append(x)
        return not stack
