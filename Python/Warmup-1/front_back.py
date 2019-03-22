'''
Given a string, return a new string where the first and last chars have been exchanged.
'''


def front_back(str):
  f = str[-1:]
  m = str[1:-1]
  b = str[:+1]
  if f == b:
    return f 
  return  f + m + b


#  front_back('code') → 'eodc'
#  front_back('a') → 'a'
#  front_back('ab') → 'ba'
