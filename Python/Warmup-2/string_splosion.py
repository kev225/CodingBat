'''
Given a non-empty string like "Code" return a string like "CCoCodCode".
'''


def string_splosion(str):
  new = ''
  i = 0
  while i <= len(str):
    new = new + str[:i]
    i += 1
  return new


#  string_splosion('Code') → 'CCoCodCode'
#  string_splosion('abc') → 'aababc'
#  string_splosion('ab') → 'aab'
