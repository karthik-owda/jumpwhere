# letter case permutation
class Solution:  
    def letterCasePermutations(self, s: str) -> list[str]:  
        result = []  

        def backtrack(sub="", index=0):  
            if len(sub) == len(s):  
                result.append(sub)  
                return  
            if s[index].isalpha():  
                backtrack(sub + s[index].swapcase(), index + 1)  
            backtrack(sub + s[index], index + 1)  

        backtrack()  
        return result  
