class Solution(object):
    def singleNumber(self, nums):
        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1

        for i in hash:
            if hash[i] != 2:
                return i
            else:
                continue
