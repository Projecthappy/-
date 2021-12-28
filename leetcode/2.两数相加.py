#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
from typing import List
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> List:
        d=[]
        jin=0
        while 
        for i in range(max(len(l1),len(l2))):
            if i>len(l1) or i>len(l2):
                z1=0
                z2=0
            else:
                z1=l1[i]
                z2=l2[i]
            zhen=(int(z1)+int(z2))%10+jin
            d.append(zhen)
            jin=(int(z1)+int(z2))//10
        return str(d).replace(" ","")
print(Solution().addTwoNumbers([2,4,3],[5,6,4]))
# @lc code=end

