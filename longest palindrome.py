#Approach 1
#TC O(n)
#SC O(1) we know there can only be 26 alphabets we store in hashmap
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmap = {}
        maxlen = 0
        flag = False
        for i in range(len(s)):
            if s[i] in hmap:
                hmap[s[i]] = hmap[s[i]]+1
            else:
                hmap[s[i]] = 1
                
        for k in hmap:
            if hmap[k] % 2 == 0:
                maxlen = maxlen + (hmap[k])
            else:
                if not flag:
                    maxlen = maxlen + (hmap[k])
                    flag = True
                else:
                     maxlen = maxlen + (hmap[k]-1)
        return maxlen

#Approach 2
#TC O(n)
#SC O(1)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        palin_set = set()
        count = 0
        for i in range(len(s)):
            if s[i] in palin_set:
                count = count+2
                palin_set.remove(s[i])
            else:
                palin_set.add(s[i])
            
        if len(palin_set) != 0:
            return count+1
        else:
            return count