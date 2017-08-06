# -*- coding:utf-8 -*-
class Solution:
    #快排牛客网超时
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput)<k or k==0:
            return []
        return self.getknum(tinput,0,len(tinput)-1,k)


    def getknum(self,tinput,s,e,k):



        mid = self.partition(tinput,s,e)

        if mid==k-1:

            return sorted(tinput[:mid+1])
        print s,mid,e
        if mid>k:
            left = self.getknum(tinput,s,mid-1,k)
            return left
        else:
            right = self.getknum(tinput,mid+1,e,k)
            return right



    def partition(self,tinput,s,e):

        x = tinput[e]
        while s<e:
            while s<e and tinput[s]<=x:
                s += 1
            tinput[s] = tinput[e]
            # print tinput
            while s<e and tinput[e]>=x:
                e -= 1
            tinput[e] = tinput[s]
        tinput[s] = x
        # print tinput,e
        return e


    def minHeap(self,tinput,k):

        res = []
        newheap = self.buildHeap(tinput)
        if k > len(tinput):
            return tinput
        for i in range(k):
            res.append(newheap.pop(0))
            # newheap.insert(0,newheap.pop(-1))
            newheap = self.buildHeap(newheap)
        return res

    def buildHeap(self,tinput):


        n = len(tinput)
        mid = n/2

        for i in range(mid,0,-1):
            left,right = 2*i-1,2*i
            tmp_index = i
            # print left,right,tmp_index,tinput[tmp_index-1]
            # print (left<n and tinput[tmp_index-1]>tinput[left]),(right<n and tinput[tmp_index-1]>tinput[right])
            while (left<n and tinput[tmp_index-1]>tinput[left]) or (right<n and tinput[tmp_index-1]>tinput[right]):
                tmp = left
                if right<n and tinput[right]<tinput[left]:
                    tmp = right
                # print tinput[tmp]
                tinput[tmp_index-1],tinput[tmp] = tinput[tmp],tinput[tmp_index-1]
                tmp_index = tmp+1
                left,right = 2*tmp_index-1,2*tmp_index
                # print left,right,tmp_index
            # print tinput
        return tinput
SS = Solution()
tinput = [4,5,1,6,2,7,3,8]
k = 4
print SS.minHeap(tinput,k)
