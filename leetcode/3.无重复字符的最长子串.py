#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max=0
        s=s+' '
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                a=s[i:j]
                if len(a)==len(set(list(a))):
                    c=j-i
                    if c>max:
                        max=c
                else:
                    break
        return max
print(Solution().lengthOfLongestSubstring(' '))
# @lc code=end

