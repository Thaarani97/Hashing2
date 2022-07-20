#TC O(n)
#SC O(n)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hmap = {0:-1}
        count = 0
        maxlen = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = count-1
            else:
                count = count+1
            if count in hmap:
                maxlen = max(maxlen,i-hmap[count])
            else:
                hmap[count] = i
                
        return maxlen
                