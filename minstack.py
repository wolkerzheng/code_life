# -*- coding:utf-8 -*-
class Solution:
    minStack = []
    stack = []
    def push(self, node):
        # write code here
        stack.append(node)
        if node < minStack.top():
        	minStack.append(node)
        else:
        	minStack.append(minStack.top())
    def pop(self):
        # write code here
        stack.pop(-1)
        minStack.pop(-1)

    def top(self):
        # write code here
        return minStack.top()
    def min(self):
        # write code here
        return minStack.top()

#c++
#  class Solution {
# public:
#     stack<int> dataStack, minStack;
#     void push(int value) {
#         dataStack.push(value);
#         if (minStack.empty()) {
#             minStack.push(value);
#         }
#         else{
#             int min = minStack.top();
#             value<=min?minStack.push(value):minStack.push(min);
#         }
#          
#     }
#     void pop() {
#         dataStack.pop();
#         minStack.pop();
#     }
#     int top() {
#         return  dataStack.top();
#     }
#     int min() {
#         return minStack.top();
#     }
# };