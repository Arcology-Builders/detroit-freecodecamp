#!/bin/python3

import math
import os
import random
import re
import sys


class Multiset:
    
    def __init__(self):
        self.counts = {}

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        if (val in self.counts):
            self.counts[val] += 1
        else:
            self.counts[val] = 1

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if (val in self.counts):
            if (self.counts[val] > 1):
                self.counts[val] -= 1
            else:
                del self.counts[val]

    def __contains__(self, val):
        return (val in self.counts)
        # returns True when val is in the multiset, else returns False
    
    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.counts)
    
if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    result = performOperations([
        'query 1',
        'add 1',
        'add 1',
        'query 1',
        'add 2'
    ])
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()