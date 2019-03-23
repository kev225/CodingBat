'''
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.
'''


def make_chocolate(small, big, goal):
  r = goal - (big*5)

  if small + (big*5)  < goal:
    return -1
    
  elif big == 0 and small < goal:
    return -1
  
  elif big*5 > goal and (goal -5 - small) > 0:
    return -1
    
  
  elif goal % 5 >= 0 and r >= 0 :
    return r
    
  elif small == goal:
      return small
      
  else:
    return goal -5


#  make_chocolate(4, 1, 9) → 4
#  make_chocolate(4, 1, 10) → -1
#  make_chocolate(4, 1, 7) → 2
