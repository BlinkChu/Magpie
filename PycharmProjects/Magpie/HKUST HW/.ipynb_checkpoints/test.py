import numpy as np

set = (1,2,3,4)
# def subsets(set):
#     if len(set) < 2:
#         return result.append((set[0]))
#     return subsets

def allSubsets(s):
    if len(s) == 0 :
        return [[]]
    return allSubsets(s[1:]) + [[s[0]] + r for r in allSubsets(s[1:])]

print(allSubsets(set))