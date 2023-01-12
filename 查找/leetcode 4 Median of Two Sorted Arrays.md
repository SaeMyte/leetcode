```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 返回数组中第k小的元素，从下标1开始计算的
        def getElementK(nums1, nums2, k):
            index1, index2 = 0, 0 # 两个数组中未被排除的开始的位置
            # 两个数组中有一个数组有空的情况
            print(index1, index2, k)
            while True:
                if index1 >= len(nums1):
                    return nums2[index2 + k - 1]
                if index2 >= len(nums2):
                    return nums1[index1 + k - 1]
                if k == 1:  # 找到了，返回两个数组中更小的那个数
                    return min(nums1[index1], nums2[index2])
                # 排除一些数字，同时需要判断下标越界
                newIndex1 = min(index1 + k // 2 - 1, len(nums1) - 1)
                newIndex2 = min(index2 + k // 2 - 1, len(nums2) - 1)
                if nums1[newIndex1] <= nums2[newIndex2]: # 排除小的那个                
                    k -= newIndex1 - index1 + 1 # 排除的是新位置到原来下标的元素个数
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1 
                    index2 = newIndex2 + 1
        m = len(nums1)
        n = len(nums2)
        k = (m+n) // 2
        if (m+n)%2 == 1: # 奇数
            return getElementK(nums1, nums2, k + 1)
        else:
            return (getElementK(nums1, nums2, k) + getElementK(nums1, nums2, k+1)) / 2
```
当m+n是奇数时，中位数的位置是(m+n)/2 + 1。当m+n是偶数时，中位数的位置是(m+n)/2和(m+n)/2+1两个位置的平均值。
找一个数组中的中位数，其实也就是找第k小的数，k为(m+n)/2 或者(m+n)/2+1。这里是从1开始计算的。
对于两个有序数组A和B，想要找到这第k个元素，比较A[k/2-1]和B[k/2-1]，其中A前面还有[0, k/2-2]， B数组前面还有[0, k/2-2]。此时对于两个其中较小的那个数，两个数组中至多只有k-2个数比它小，因此这个数组中[0, k/2-1]可以排除掉。在排除后的新数组上继续进行二分查找。(每一次都要更新k，每次都排除k/2个数)
1. 某个数组为空，说明数组中所有元素被排除，返回另一个数组中第k小的数
2. 如果下标k/2-1越界，选择数组中的最后一个数，并且根据此时排除数组的个数更新k的值。
3. 如果k=1，说明此时找到第k小的数，返回两个数组中未被排除的数组中的更小值。
