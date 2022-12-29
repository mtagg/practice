class Solution(object):

        
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # make a dic to store index values, with a search in O(1) time\
        indicies = {} 
        for i in range(len(nums)):
            if indicies.get(target-nums[i]) != None:
                return [i, indicies[target-nums[i]]]
            else:
                indicies[nums[i]] = i                
        return []