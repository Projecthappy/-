#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        i,max=0,1
        chuan=''
        s=s+' '
        while i<len(s)-max:
            maxstep=min(len(s)-i-1,i)
            step=max
            while step<=maxstep:
                if step==0:
                    s1=s[i]
                else:
                    s1=s[i-step:i+step+1+1]
                if s1[::-1]==s1:
                    max=len(s1)
                    chuan=s1
                step=step+1
            i=i+1
        return chuan
print(Solution().longestPalindrome('babad'))

# @lc code=end

