# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if array==None or len(array)==0:
            return 0
        
        ndict = {}
        res = []
        for n in array:
            ndict[n]=ndict.get(n,0)+1
        for i in range(len(array)):
            if ndict[array[i]] == 1:
                res.append(array[i])
                if len(res)==2:
                    break
            
        return res