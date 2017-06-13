# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array == None or len(array)==0:
            return False
        row,col = len(array),len(array[0])
        i,j = 0,col-1
        while i<row and j>=0:
                if array[i][j] == target:
                    return True
                elif array[i][j] < target:
                    i+=1
                else:
                    j-=1
        return False
