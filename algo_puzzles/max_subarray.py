# Invariant for auxiliary data structure
# begin[i] up to and including i, what is the beginning index of max subarray starting from 0
# end[i] up to and including i, what is the ending index of maximum subarray starting from 0

# Base Case
## when you are beginning the list, the max subarry begin[0] = end[0] = 0
# Inductive Case
## when you already have a subarray up to begin[i] and end[i]
## how to add begin[i+1] and end[i+1]
## cases:
## if end[i] == i, then i+1 could potentially increase and be the new max subarray
## does begin[i] matter? how do we know we are beginning a new max subarray?
## only if a subarray grows negative, then they don't accumulate

## we might need a 2D array of subarrays beginning at each i and ending
## for each j, we mostly copy over 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        