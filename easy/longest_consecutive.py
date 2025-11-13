class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        lon =0

        nums = set(nums)

        for i in nums:
            leng = 1

            if i-1 not in nums:
                cur = i

                while cur+1 in nums:
                    leng += 1
                    cur +=1

                lon = max(leng, lon)

        

        return lon
        






        
