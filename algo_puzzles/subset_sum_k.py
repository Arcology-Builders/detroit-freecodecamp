# Hello from Paul
# Try to Replit for next problem
# 560. Subarray Sum Equals K

"""
Given an array of integers `nums` and an integer `k`,
return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 0:

[1, 1], k =2

Output: 1


Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

# Brute Force
# Quadratic time, O(N^2), slower


# Time Complexity (CPU), lower function is faster / better
# Linear time, O(N), where N = size of your input, nums.length

# Sliding Window
# keep track of
# - back pointer {      "i" 
# - forward pointer }   "j"

         _
  0   1  2  3  4  5
[ 1 , 1, 1, 1, 0, 1 ]  k=3
      ij

3

INVARIANT: a condition you want to always be true
aux[i] = number of subarrays from the original array, starting from index 0 up to (and including) index i
         that sum up to k

RADIX SORT IDEA:
Invariant:
sums[i] = number of arrays that sum to that number

length of sums = O(k), 10 million , O(N)
end = 2
# count = 0
# v = k - 1 = 2
# sums_0 = [0, 1, 2, 3, 4, ... ]
            0  1  0  0  0

for v from 0 up to k, inclusive
v = k - 1 = 2
sums_1 = [0, 1, 2, 3, 4, ... ]
          0  1  1  0
count = 1

sums_2 = [0, 1, 2, 3, 4, ]
             
count = 2

sums_3 = [0, 1, 2, 3, 4, ]
             1  1
count = 3

sums_4 = [0, 1, 2, 3, 4, ]
          1  1  1
count = 3

sums_5 = [0, 1, 2, 3, 4, ]
             1  1
count = 4

only increment count, if nums[n-1] != 0, and nums[n-1] + v = k

Pseudocode for one execution of subarraySumsHelper, at nums[i]

# O(1)
# Base case: solve for an array of length 1,
#    take the value nums[0]
#      if it's k, then return 1
#      otherwise, then return 0

# O(k)
# Inductive case: assume you have a solution sums for nums[0:n-1]
#    end = max(end, nums[n-1])
#    v = k - nums[n-1]
#    ??
#    if ???:
#      sums[k] += 1
#    sums[nums[n-1]] += 1 # single item subarray of nums[n-1] itself

#    for v in (k - nums[n-1] downto 0) inclusive
#      sums[v] += 

How many subproblems do we have? One per location in original nums
# O(N) * max(O(1), O(k)) = O(Nk)

O(N) space = sums, nums, count O(1), end O(1)
O(N) time

sums[1] = 1


[0, 1, ] 

Auxiliary Table (candidate) at each index i, contains the sum of the subarray
from the original nums input index i, all the way to the end (nums.length -1)
  0   1   2  3
[ 6 ,4 , 1, 0 ]  you only need to go back in aux up to k - nums[nums.length-1]
        <- k ->  N times, building up aux table

sum from 0 to the end (1)
     sum from 1 to the end(1)

O(N) space (extra auxiliary table)
O(N*K) time

nums[2] is 1. what can we add to it to equal k=2?
brute force
aux[0] is already 2, no good, 2+1 = 3
aux[1] is 1, 1+1 = 2  GOOD

Dynamic Programming
[ ? , ? , ? ]

Example 2:

Input: nums = [1,2,3], k = 3
                   ij
Output: 2

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

class Solution:

    
    # [1,1,1] k =2

    # [0,0,0], 1, k=2
    def subarraySumHelper(self, old_sums, new_item, k):
        new_sums = [0 for i in range(k)]  # [0,0,0]
        new_count = 0                     # 0
        for v in range(k):    # 0, 1, 2
            if (v >= new_item):
                new_sums[v-new_item] = old_sums[v]  # [0 ]

        if (v != 0) and v == (k - new_item):
            new_count += 1

        new_sums[new_item] = 1
        return (new_sums, new_count)

    def subarraySum(self, nums, k):
        sums = [0 for i in range(k)]
        count = 0
        for i in range(len(nums)):
            (new_sums, new_count) = self.subarraySumHelper(sums, nums[i], k)
            sums = new_sums
            count += new_count
        return count

"""
    # invariant: aux[i] = number of subarrays within nums[0] to num[i] inclusive that sum to k
    # len(aux) = 1 (at least a single item aux table)
    # Meaning: subarraySumHelper(aux, nums[n-1], k) == aux[n-1]
    def subarraySumHelper(self, aux, new_item, k):
        count = 0
        z = len(aux)-1 #
        # special case: the new item is k by itself
        if new_item == k:
            return 1
        # runs in O(k), but what about if you have a bunch of zeros?
        while z >= 0 and (aux[z] + new_item <= k):
            if new_item + aux[z] == k:
                count += 1
            aux[z] += new_item
        return count

    # [1, 1, 1]
    def subarraySum(self, nums, k):
        count = 0

        if (len(nums) == 1):
            if nums[0] == k:
                return 1
            return 0
        else:
            
            aux = [nums[0]]
            super_count = 0
            # for i in range 1, to 3
            for i in range(1, len(nums)):
                # i = 1, self.subarraySumHelper([], 1, 2)
                # Count of new subarrays that sum to k up to index i
                sub_count = self.subarraySumHelper(aux, nums[i], k)
                aux.append(sub_count) # now aux has length i
                super_count += sub_count
            return super_count
"""

# I think you need to update the aux table each time, but only back by O(k)

"""         for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums)-1, i-1, -1):
        
                if k == sum(nums[i: j+1]):
                    count += 1

        return count
 """
s = Solution()
soln1 = s.subarraySum([1,1,1], 2)
print(soln1)
assert(soln1 == 2)

soln2 = s.subarraySum([1,2,3], 3)
print(soln2)
assert(soln2 == 2)