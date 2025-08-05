class Solution(object):
    def findClosestNumber(self, nums):
        """
        
        :type nums: List[int]
        :rtype: int
        """
        dist = nums[0]

        for i in range(1,len(nums)):
            if abs(dist) > abs(nums[i]):
                dist = nums[i]
            elif abs(dist) == abs(nums[i]):
                if nums[i]> dist:
                    dist = nums[i]

        return dist
            
            