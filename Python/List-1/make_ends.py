'''
Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.
'''


def make_ends(nums):
  new = [nums[0], nums[-1]]
  return new


#  make_ends([1, 2, 3]) → [1, 3]
#  make_ends([1, 2, 3, 4]) → [1, 4]
#  make_ends([7, 4, 6, 2]) → [7, 2]
