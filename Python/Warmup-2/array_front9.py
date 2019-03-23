'''
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
'''


def array_front9(nums):
  for i in nums:
    if i == 9 and nums.index(9) <3:
      return True
  return False


#  array_front9([1, 2, 9, 3, 4]) → True
#  array_front9([1, 2, 3, 4, 9]) → False
#  array_front9([1, 2, 3, 4, 5]) → False
