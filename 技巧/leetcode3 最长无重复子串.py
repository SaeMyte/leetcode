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
