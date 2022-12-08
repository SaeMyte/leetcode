## 异或运算做两个数的交换

可以理解成无进位相加
1)0 ^ N = N
N ^ N = 0
2)交换律和结合律
3) 交换两个数: a和b可以值相等，但是必须保证a和b指向不同的内存(一个内存区域自身异或，会变为0)
```
 a = a^b;  a = a^b   b = b
 b = a^b;  a = a^b   b =  a^b^b = a^0 = a
 a = a^b;  a = a^b^a = b^0 = b
```
### 例1 
已知一个数组中只有一种数出现了奇数次，其他所有数都出现了偶数次
1）怎么找到出现了奇数次的数
```
"""
用异或操作找出一个数组中只出现了奇数次的数
思路：将这个数组依次异或，
input: 1 5 6 5 1 7 7
偶数次的数字均为0
"""

def FindDigtal(nums):
    result = 0
    if len(nums) == 0:
        return -1
    for data in nums:
        result = result ^ data
    return result
if __name__=='__main__':
    nums = [1,5,6,5,1,7,7]
    print(FindDigtal(nums))
```
**2）在数组中如果有两种数出现了奇数次，其他都出现了偶数次，怎么找到这两种数。**
[时间复杂度O(n),空间复杂度O(1)]

```
"""
没想出来
两个奇数次的数，从前往后遍历一次异或结果为  c1 = a ^ b
c1的二进制数上至少有一位不为0,假设是第八位，则a和b在第八位上一定是不一样的。
数组中可以分为两类：a和b分在了两个集合中
1）第八位是1： 出现偶数次的数， a
2）第八位是0   出现偶数次的数， b


"""
def FindDigtal(nums):
    eor = 0
    for data in nums:
        eor = eor ^ data
    # eor必然有一个位置为1，选择最低为的1
    rightOne = eor & (-eor) #负数是补码存储，也就是~eor+1 ， 获取lowbits[一个数最右侧的1]
    onlyOne = 0  # eor'
    for data in nums:
        if data & rightOne == 0:
            onlyOne = onlyOne ^ data
    a = onlyOne
    b = eor ^ onlyOne
    return a, b
if __name__=='__main__':
    nums = [1,5,6,5,1,7,7,7]
    print(FindDigtal(nums))
```
