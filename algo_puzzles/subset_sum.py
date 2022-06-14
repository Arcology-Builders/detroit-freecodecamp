#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

# We need logarithmic search to find the closest key to a given key,
# if it's missing, or that exact key if it's present.

class BinaryTree:
    
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def getClosestGreaterThan(self, key):
        if (self.key > key):
            return None
        if self.key <= key:
            if (self.right is None):
                return (self.key, self.value)
            return self.right.getClosestGreaterThan(key) or (self.key, self.value)

    def getClosestLessThan(self, key):
        if (self.key < key):
            return None
        if self.key >= key:
            if (self.left is None):
                return (self.key, self.value)
            return self.left.getClosestLessThan(key) or (self.key, self.value)

    def contains(self, key):
        if self.key == key:
            return True
        if (key < self.key):
            return ((self.left is not None) and self.left.contains(key))
        elif (key > self.key):
            return ((self.right is not None) and self.right.contains(key))
        
    def insert(self, key, value):
        if (key == self.key):
            raise ValueError("Cannot replace value for key " + key)
        if (key < self.key):
            if (self.left is None):
                self.left = BinaryTree(key, value)
            else:
                self.left.insert(key, value)
        elif (key > self.key):
            if (self.right is None):
                self.right = BinaryTree(key, value)
            else:
                self.right.insert(key, value)
                

        

# A data structure which lets you search by a right key
class MemoRightRange:
    
    def __init__(self):
        self.rangeSums = {} # key right index -> (key left index -> (sums, zeros)
    
    def addRange(self, rightIndex, leftIndex, numbers):
        if (rightIndex):
        

def findSum(numbers, queries):
    # Write your code here
    q = len(queries)
    
    # Memoize results of queries to save time
    memos = {} # key is tuple (l, r) -> value tuple (sum of numbers[l..r], number of zeros)
    
    results = [0 for i in range(q)]
    for i in range(q):
        l = queries[i][0]
        r = queries[i][1]
        sumlr = 0
        zeros = 0
        if ((l,r) in memos):
            (sumlr, zeros) = memos[(l,r)]
        else:            
            for j in range(queries[i][0], queries[i][1]+1):
                # 1-indexed, so subtract 1 from j
                if numbers[j-1] == 0:
                    zeros += 1
                else:
                    sumlr += numbers[j-1]
            memos[(l,r)] = (sumlr, zeros)
        results[i] = sumlr + (zeros * queries[i][2])
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    result = findSum(numbers, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
