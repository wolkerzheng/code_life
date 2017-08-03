#encoding=utf8
def divede(nums):

    if len(nums) <= 1:
        return nums
    l = len(nums)/2
    left = divede(nums[:l])
    right = divede(nums[l:])

    sortnum = merge(left,right)
    return sortnum

def merge(left,right):

    i,j=0,0

    l1,l2 = len(left),len(right)
    nums = []
    while i<l1 and j<l2:
        if left[i]<right[j]:
            nums.append(left[i])
            i+=1
        else:
            nums.append(right[j])
            j+=1
    if i<l1:
        nums.extend(left[i:])
    if j<l2:
        nums.extend(right[j:])
    return nums

print divede([2,3,112,122,12,6])
