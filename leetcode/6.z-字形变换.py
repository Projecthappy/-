#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)>2 and numRows>1:
            b=numRows*2-2
            s=s+' '*(b-(len(s)-numRows)%b)
            z=s[::b]
            a=(len(s)-numRows)//(b)
            for i in range(1,numRows-1):
                z=z+s[i]
                for j in range(1,a+1):
                    end=i+j*b
                    z=z+s[end-i*2]+s[end]
            z=z+s[numRows-1::b]
            return z.replace(' ','')
        else:
            return s
# @lc code=end
print(Solution().convert("A",1))
#另一种排列顺序
