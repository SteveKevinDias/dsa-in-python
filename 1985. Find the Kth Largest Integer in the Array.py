class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        #sort the array
        for i in range(0,len(nums)):
            nums.append(int(nums[i]))
            x = nums[i]
            nums[i] = nums[-1]
            nums.pop()
           

        sorted_nums = nums.sort()
        return str(nums[len(nums) - k])
