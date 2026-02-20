class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """

        # nums = [1,3,5,2,7,5], minK = 1, maxK = 5

        lastmin = -1
        lastmax = -1
        lastinv = -1
        reward = 0

        for i in range(len(nums)):

            if nums[i] == minK:
                lastmin = i

            if nums[i] == maxK:
                lastmax = i

            if nums[i] < minK or nums[i] > maxK:
                lastinv = i

            temp = min(lastmin, lastmax) - lastinv # - last inv
            # bcz it gives you how many steps behind you can go in awway before you min() hence increasing variations. 
            reward = reward + temp if temp>0 else reward + 0

        return reward

            


            

            
