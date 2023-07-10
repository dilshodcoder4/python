# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
def not_poor(word):
  snot = word.find('not')
  spoor =word.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    word = word.replace(word[snot:(spoor+4)], 'good')
    return word
  else:
    return word
print(not_poor('Mr Thomas is not that poor!'))

#>>> Mr Thomas is good!