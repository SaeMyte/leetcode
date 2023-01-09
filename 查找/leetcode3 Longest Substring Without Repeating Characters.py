class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 使用哈希表来检索有无重复
        ch = list()
        result = 0 # 用来记录无重复字串的最大长度
        sum = 0
        for i, data in enumerate(s):
            if data not in ch:
                sum += 1
            else: # 找到重复的字符，清空从哈希表开始到重复的那一个
                # 更新结果
                result = max(result, sum)
                # 删除从开始到那个重复字符
                while ch:
                    t = ch[0]
                    ch.pop(0)
                    if t == data:
                        break
            # 无论是否更新，当前这个字符一定要入哈希表
            ch.append(data)
            sum = len(ch)
        result = max(result, sum)
        return result
"""
官方解法是使用滑动窗口
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 使用哈希表来检索有无重复
        map = dict() # <字符，字符位置+1>，其实存放的是与当前字符重复的下一个位置，下一个位置是这个子串的起始
        start = 0
        end = 0
        maxLen = 0
        sum = 0
        while end < len(s):
            # 如果当前字符不在哈希表中，意思是无重复
            if s[end] not in map:
                map[s[end]] = end + 1
            # 如果当前字符在哈希表中，更新start为上一个重复字符的后一位
            else:
                start = max(start, map[s[end]])
                map[s[end]] = end + 1 
            # 更新结果
            maxLen = max(maxLen, end - start + 1)
            end = end + 1
        return maxLen
