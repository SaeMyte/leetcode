# 递归行为和递归时间复杂度
## 1.用递归方法求一个数组中的最大值（递归版本）
### 求中点位置:
 mid = (L+R)/2
 数组很大，L+R会溢出。
 mid = L + (R-L)/2
 简化: mid = L+(R-L)>>1  [右移等于除2]
```
def FindMax(nums, L, R):
    if L == R:
        return nums[L]
    mid = L + ((R-L)>>1) #防止溢出的中点的写法
    LeftMax = FindMax(nums, L, mid)
    RightMax = FindMax(nums, mid+1, R)
    return max(LeftMax, RightMax)
if __name__=="__main__":
    nums = [3,5,1,9,10,15,0]
    print(FindMax(nums, 0, len(nums)-1))
```
## master公式
T(N)=a*T(N/b)+O(N^d)
母问题数据量是N级别的，a是子问题的调用次数，O(N^d)是除子问题调用外剩下的过程时间复杂度。
### 上述问题的master公式
T(N)=2*T(N/2)+O(1)
**子问题规模不同则不符合master公式**
