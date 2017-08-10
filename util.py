#encoding=utf8
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bfs(root):
	if root:
		queue = []
		queue.append(root)
		while queue:
			q = queue.pop(0)
			if q.left:
				queue.append(q.left)
			if q.right:
				queue.append(q.right)
			print q.val
def dfs(root):
	if root:
		stack = []
		stack.append(root)
		while stack:
			s = stack.pop(-1)
			if s.right:
				stack.append(s.right)
			if s.left:
				stack.append(s.left)
			print s.val

def BuildTree(nums,idx):

	if nums == None or len(nums)==0 or idx>len(nums):
		return None
	if nums[idx-1] == '#':
		return None

	root = TreeNode(nums[idx-1])
	root.left = BuildTree(nums,2*idx)
	root.right = BuildTree(nums,2*idx+1)
	return root
# nums = [1,2,3,4,5,6,7,8,'#',10,'#']
# root =  BuildTree(nums,1)
# bfs(root)
# dfs(root)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def BuildListNode(nums):

	tmpHead = ListNode(-1)
	if nums is None or len(nums)<=0:
		return tmpHead.next
	
	
	res = tmpHead
	for n in nums:
		p = ListNode(n)
		tmpHead.next = p
		tmpHead = tmpHead.next 
	
	return res.next

def printListNode(listnode):

	if not listnode:
		return None
	res=[]
	while listnode:
		res.append(listnode.val)
		listnode = listnode.next
	# print res
	return res

if __name__ == '__main__':
	
	print printListNode(BuildListNode([1,1,2,3,3,3,4,4,5]))
