from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # will help me keep track of my longest substring
        count = Counter()

        # pointers to create longest
        left = 0
        # base case if we're handed an empty string
        best = 0

        #loop through word 
        for rtidx in range(len(s)):
            #put in my counter obj
            count[s[rtidx]]+=1

            # checking if duplicate
            while count[s[rtidx]] > 1:
                # elim it from counter ojb
                count[s[left]]-=1
                # now must move my left pointer forward to continue searchign
                left += 1
            # getting the best length
            best = max(best, rtidx - left + 1) # right - left + 1 makes sense because we're keeping track of length
        
        return best
                
    

        