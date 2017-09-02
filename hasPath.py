# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here

        if matrix is None or rows<1 or cols <1 or not path:
        	return False

 		visited = [False]*cols*rows
 		patgLength = 0

 		for i in range(rows):

 			for j in range(cols):

 				if(self.hasPathHelp(matrix, rows, cols,i,j path,patgLength,visited)):
 					return True
 		return False


    def hasPathHelp(self,matrix, rows, cols, r,c,path,patgLength,visited):

    	if patgLength==len(path):
    		return True

    	flag = False

    	if r<rows and r>=0 and c<cols and c>=0 and matrix[r*cols+c] == path[patgLength] and not visited[r*cols+c]:
    		patgLength += 1
    		visited[r*cols+c] = True
    		flag = self.hasPathHelp(matrix, rows, cols, r,c-1,path,patgLength,visited) or
    			self.hasPathHelp(matrix, rows, cols, r,c+1,path,patgLength,visited) or
    			self.hasPathHelp(matrix, rows, cols, r-1,c,path,patgLength,visited) or
    			self.hasPathHelp(matrix, rows, cols, r+1,c,path,patgLength,visited) or
    		if not  flag:
    			patgLength -= 1
    			visited[r*cols+c] = False
    	return flag


S = Solution()
print S.hasPath()



# java基本思路：回溯
# import java.util.Arrays;
# public class Solution {
#   public boolean hasPath(char[] matrix, int rows, int cols, char[] str) {
#  
#         if (matrix == null || rows < 1 || cols < 1 || str == null) {
#             return false;
#  
#         }
#         boolean[] visited = new boolean[rows * cols];
#         Arrays.fill(visited, false);
#         int pathLength = 0;
#         for (int row = 0; row < rows; ++row) {
#             for (int col = 0; col < cols; ++col) {
#                 if (hasPathCore(matrix, rows, cols, row, col, str, pathLength,
#                         visited)) {
#                     return true;
#  
#                 }
#             }
#  
#         }
#         return false;
#  
#     }
#  
#     boolean hasPathCore(char[] matrix, int rows, int cols, int row, int col,
#             char[] str, int pathLength, boolean[] visited) {
#         if (pathLength == str.length) {
#             return true;
#         }
#         boolean hasPath = false;
#         if (row >= 0 && row < rows && col >= 0 && col < cols
#                 && matrix[row * cols + col] == str[pathLength]
#                 && !visited[row * cols + col]) {
#             ++pathLength;
#             visited[row * cols + col] = true;
#             hasPath = hasPathCore(matrix, rows, cols, row, col - 1, str,
#                     pathLength, visited)
#                     || hasPathCore(matrix, rows, cols, row - 1, col, str,
#                             pathLength, visited)
#                     || hasPathCore(matrix, rows, cols, row, col + 1, str,
#                             pathLength, visited)
#                     || hasPathCore(matrix, rows, cols, row + 1, col, str,
#                             pathLength, visited);
#  
#             if (!hasPath) {
#  
#                 --pathLength;
#                 visited[row * cols + col] = false;
#  
#             }
#         }
#         return hasPath;
#  
#     }
#  
#  
# }