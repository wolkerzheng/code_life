# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
         # if number == 1:
         # 	return 1
         if number <= 2:
         	return number
         return self.rectCover(number-1)+self.rectCover(number-2)
         pass



S = Solution()

test = [1,2,3]

for t in test:
	print S.rectCover(t)