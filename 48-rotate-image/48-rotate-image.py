class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rotate_Matrix=[]
        for i in range(len(matrix)):
            L=[]
            for j in range(len(matrix)):
                L.append(matrix[j][i])
            L.reverse()
            rotate_Matrix.append(L)
            
            
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]=rotate_Matrix[i][j]