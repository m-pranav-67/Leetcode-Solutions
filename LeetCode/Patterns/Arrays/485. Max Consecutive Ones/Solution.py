class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        m_c = 0
        for i in range(n):
            co = 0 
            for j in range(i,n):
                if nums[j] == 1:
                    co += 1 
                    m_c = max(m_c, co)
                else: 
                    break
        return m_c