class Solution(object):
    def searchMatrix(self,matrix, target):
        m = len(matrix)   
        n = len(matrix[0])   
        row, col = 0, n - 1   

        while row < m and col >= 0:
            value = matrix[row][col]
            if target == value:
                return True
            elif target < value:
                col -= 1   
            else:
                row += 1   
        return False


        