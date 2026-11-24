class Solution(object):
    def longestConsecutive(self, nums):
        nset = set(nums)
        lng = 0
        for i in nset:
            if i - 1 not in nset:
                currn=i
                c=1
                while currn + 1 in nset:
                    currn += 1
                    c += 1
                lng = max(lng , c)
        return lng     
        