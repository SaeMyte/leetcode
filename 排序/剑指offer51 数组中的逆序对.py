#RuntimeError:maximum recursion depth exceeded
#错误原因： if L == R; 必须是L >= R
#一定要注意边界条件
"""
def MergeSort(nums, L, R):
    if L == R:  
        return 0  #数组中只有一个元素，不需要再排序
    mid = L +((R-L)>>1)  #特殊的写法，防溢出
    #逆序对等于左边的逆序对+右边的逆序对+归并的逆序对
    return MergeSort(nums, L, mid) + MergeSort(nums, mid+1, R) +Merge(nums, L, mid, R)

def Merge(nums, L, mid, R):
    #准备一个辅助空间
    nums1 = []
    sum = 0
    i = L
    j = mid + 1
    while i <= mid and j <= R:
        if nums[i] <= nums[j]:  #左侧比右侧小，加右侧，不做处理
            nums1.append(nums[j])
            j += 1
        else:   #左侧比右侧大，加左侧
            nums1.append(nums[i])
            sum = sum + (R-j+1)
            i += 1
    if i > mid:
        for data in nums[j:R+1]:
            nums1.append(data)
    if j > R:
        for data in nums[i: mid+1]:
            nums1.append(data)
    for i in range(0, len(nums1)):
        nums[L+i] = nums1[i]
    return sum
    
if __name__=="__main__":
    nums = [7,5,6,4]
    minAnd = MergeSort(nums, 0, len(nums)-1)
    print(minAnd)
"""

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def MergeSort(L, R):
            if L >= R:
                return 0  #数组中只有一个元素，不需要再排序
            mid = L +((R-L)>>1)  #特殊的写法，防溢出
            res = 0
            #逆序对等于左边的逆序对+右边的逆序对+归并的逆序对
            res += MergeSort(L, mid) 
            res += MergeSort(mid+1, R) 
            nums1 = []
            i = L
            j = mid + 1
            while i <= mid and j <= R:
                if nums[i] <= nums[j]:  #左侧比右侧小，加左侧，不做处理
                    nums1.append(nums[i])
                    i += 1
                else:   #左侧比右侧大，加右侧
                    nums1.append(nums[j])
                    j += 1
                    res = res + (mid-i+1)
            if i > mid:
                for data in nums[j:R+1]:
                    nums1.append(data)
            if j > R:
                for data in nums[i: mid+1]:
                    nums1.append(data)
            for i in range(0, len(nums1)):
                nums[L+i] = nums1[i]
            return res
        return MergeSort(0, len(nums)-1)
