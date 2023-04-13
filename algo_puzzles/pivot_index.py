def updateLeftSum(index, nums, sums):
    if (index <= 0):
        sums[index] = 0
    else:
        sums[index] = sums[index-1] + nums[index-1]

def updateRightSum(index, nums, sums):
    if (index >= len(nums) - 1):
       sums[index] = 0
    else:
        sums[index] = sums[index+1] + nums[index+1]

def computeSums(nums):
    leftSums = [0 for x in nums]
    rightSums = [0 for x in nums]
    left = 0
    right = len(nums) - 1
    for x in range(len(nums)):
        left = x
        right = len(nums) - x - 1
        updateLeftSum(left, nums, leftSums)
        updateRightSum(right, nums, rightSums)
    return (leftSums, rightSums)


class Solution:
    def pivotIndex(self, nums):

        (leftSums, rightSums) = computeSums(nums)

        for i in range(len(nums)):
            if (leftSums[i] == rightSums[i]):
                return i
        
        return -1

soln = Solution()
ex1 = [1,7,3,6,5,6]
print(computeSums(ex1))
assert(3 == soln.pivotIndex(ex1))

ex2 = [2,1,-1]
print(computeSums(ex2))
assert(0 == soln.pivotIndex(ex2))
