#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l3=nums1+nums2
        l3.sort()
        z=len(l3)//2
        if len(l3)%2==0:
            mid=(int(l3[z])+int(l3[z-1]))/2
        else:
            mid=int(l3[z])
        return mid
print(Solution().findMedianSortedArrays([1,3],[2]))
# @lc code=end

