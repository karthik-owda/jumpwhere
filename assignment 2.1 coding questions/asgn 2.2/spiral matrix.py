# spiral matrix
class Solution:
    def spiralMatrix(self, matrix: list[list[int]]) -> list[int]:  
        result = []  
        while matrix:  
            result.extend(matrix.pop(0))  
            if matrix and matrix[0]:  
                for row in matrix:  
                    result.append(row.pop())  
            if matrix:  
                result.extend(matrix.pop()[::-1])  
            if matrix and matrix[0]:  
                for row in reversed(matrix):  
                    result.append(row.pop(0))  
        return result  
    
