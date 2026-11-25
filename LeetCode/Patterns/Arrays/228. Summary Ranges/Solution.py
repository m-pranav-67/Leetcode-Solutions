class Solution(object):
    def summaryRanges(self, nums):
        res = []
        i = 0
        while i<len(nums):
            st = nums[i]
            while i+1 <len(nums) and nums[i+1] == nums[i]+1:
                i+=1
            end=nums[i]
            if st == end:
                res.append(str(st))
            else:
                res.append(str(st)+"->"+str(end))
            i+=1
        return res
        