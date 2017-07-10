# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if data == None or len(data)==0:
            return 0
        count =0
        start,end = 0,len(data)-1
        
        while start<=end:

            mid = (start+end) / 2
            print mid
            if data[mid]<k:
                start = mid+1
            elif data[mid]>k:
                end = mid-1
            if data[mid]==k:
                count += 1
                i = mid
                while i+1<=end and data[i+1]==k:
                    i+=1
                    count += 1
                while mid>start and data[mid-1]==k:
                    mid-=1
                    count +=1
                return count 
        return count 


ss = Solution()
k = 5
data = [1,2,3,5,5,5,5,8]
print ss.GetNumberOfK(data,k)