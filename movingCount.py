# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        res = 0
        vis = [False]*rows*cols
        return self.movingCountHelp( threshold, rows, cols,0,0,vis)
    
    def movingCountHelp(self, threshold, rows, cols,r,c,vis):

    	count = 0
    	if self.check(threshold,rows,cols,r,c,vis):
    		vis[r*cols+c] = True
    		count = 1+self.movingCountHelp(threshold,rows,cols,r,c+1,vis)+self.movingCountHelp(threshold,rows,cols,r,c-1,vis)+self.movingCountHelp( threshold, rows, cols,r-1,c,vis)+self.movingCountHelp( threshold, rows, cols,r+1,c,vis)

    	return count
    
    def getSum(self,n):

   		res = 0
   		while n>0:
   			res += n%10
   			n = n/10
   		return res

    def check(self,threshold, rows,cols,i,j,visited):

    	if i>=0 and j>=0 and rows>i and cols>j and not visited[i*cols+j] and (self.getSum(i)+self.getSum(j))<=threshold:
    		return True
    	return False


SS = Solution()
# print  SS.movingCount(10,1,100) #29
print SS.movingCount(15,20,20)	#359


# # -*- coding:utf-8 -*-
# class Solution:
#     def movingCount(self, threshold, rows, cols):
#         # write code here
#         visit = [0]*rows*cols
#         #创建一个跟方格一样大小的矩阵，并且初始化元素全是False
#         for i in range(rows*cols):
#             visit[i] = False
#         count = self.movingCountCore(threshold, rows, cols, 0, 0, visit)
#         return count
#          
#     def movingCountCore(self, threshold, rows, cols, row, col, visit):
#         count = 0
#         #如果这一个满足条件，即数位之和不大于K，且下标各种不能越界且没有来过，那就可以走啦
#         if (self.check(threshold, rows, cols, row, col, visit)):
#             visit[row * cols + col] = True
#             #上下左右走一遭
#             count = (1 + self.movingCountCore(threshold, rows, cols, row-1, col, visit)
#             + self.movingCountCore(threshold, rows, cols, row, col-1, visit)
#             + self.movingCountCore(threshold, rows, cols, row+1, col, visit)
#             + self.movingCountCore(threshold, rows, cols, row, col+1, visit))
#         return count
#     #判断这一步能不能走
#     def check(self,threshold, rows, cols, row, col, visit):
#         if (row >= 0 and row < rows and col >= 0 and col < cols and self.getDigitSum(row) + self.getDigitSum(col) <= threshold and not visit[row*cols+col]):
#             return True
#         return False
#     #判断数位之和是否大于k
#     def getDigitSum(self, number):
#         sum = 0
#         while number > 0:
#             sum += number % 10
#             number /= 10
#         return sum