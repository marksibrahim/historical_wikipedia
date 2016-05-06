import re

def get_year_actual(x, round2):
  x = x.strip()

  # If this word is only in Old English
  if x == 'OE':
    return [10, 10]

  # If this word is Old English till now
  if x == 'OE-':
    return [10, 2015]

  # Special exception to get rid of
  if x == 'OE- Law':
    return [10, 2015]

  # Special exception to get rid of
  if x == 'OE- fig.':
    return [10, 2015]

  # Special exception to get rid of
  if x == 'OE- rare':
    return [10, 2015]

  # Special exception to get rid of
  if x == 'OE-1563-':
    return [10, 2015]

  # If this word starts in Old English and then ends
  if x.startswith('OE-'):
    if x[3:].replace(' ', '').replace('.', '').replace('&', '').isalpha():
      return [10, 2015]
    if len(x) == 7:
      return [10, int(x[3:])]
    elif len(x) == 8:
      return [10, int(x[-4:])]
  #  else:
  #    return [0, 0]

  # If this word is only in Old English
  #if x.startswith('OE'):
  #  #if not x[2:].replace(' ', '').isalpha():
  #  #return [10, 2015]
  #  #return ''

  # Deal with any slashes in the string
  i = x.find('/')
  while i > -1:
    for j in range(i+1, len(x)):
      if not x[j].isdigit() or x[j] == '-':
        x = x[:i] + x[j:]
        break
    if j == len(x)-1:
      x = x[:i]
    i = x.find('/')

  # Remove parenthesis
  if '(' in x and ')' in x:
    x = x[:x.find('(')] + x[x.find(')')+1:]

  # If there is just four digits
  if len(x) == 4 and x.isdigit():
    return [int(x), 2015]
    #return ''
  
  # This next secion cuts of alpha characters at the end of the year
  x_back = x[::-1]
  
  tmp = re.search(r'\d', x_back)
  if tmp != None:
    i = len(x) - tmp.start()
  else:
    i = 0
  
  tmp = re.search(r'-', x_back)
  if tmp != None:
    j = len(x) - tmp.start()
  else:
    j = 0

  k = int(max(i, j))
  if k == 0:
    k = len(x)
  x = x[:k+1].strip()

  if x.startswith('c'):
    x = x[1:]
  elif x.startswith('a'):
    x = x[1:]

  # Check again for Old English after removing weird stuff
  if x.startswith('OE-'):
    if x[3:].replace(' ', '').replace('.', '').replace('&', '').isalpha():
      return [10, 2015]
    if len(x) == 7:
      return [10, int(x[3:])]
    elif len(x) == 8:
      if not x == 'OE-1706-':
        return [10, int(x[-4:])]

  # Now check again if we have just four digits
  if len(x) == 4 and x.isdigit():
    return [int(x), 2015]

  # Check if we have four digits and a dash
  if len(x) == 5 and x[-1:] == '-':
    return [int(x[:4]), 2015]

  # Check if we have a start and end date
  if len(x) == 9 and x[4:5] == '-':
    return [int(x[:4]), int(x[5:])]

  # Check if we have a start and end date with c or a (ignore a dash at the end)
  if len(x) == 10 and x[4:5] == '-':
    if x[5:6] == 'c' or x[5:6] == 'a':
      return [int(x[:4]), int(x[6:])]
    else:
      return [int(x[:4]), int(x[5:-1])]

  return [0, 0]

def get_year(x):
  x = x.strip()

  y = get_year_actual(x, False)

  if y != [0, 0]:
    return y

  if x.find('+') > -1:
    x2 = get_year_actual(x[:x.find('+')], True)
    if x2 != [0, 0]:
      return x2

  return [0, 0]

def get_actual_words(words, depth=0):
  made_changes = False
  new_words = []
  for word in words:
    if '(' in word:
      # Catches things like 'a(i)glet'
      # Don't add what in the parens
      new_word = word[:word.find('(')] + word[word.find(')')+1:]
      new_words.append(new_word.strip())
      # Do add whats in the parens
      new_word = word[:word.find('(')] + word[word.find('(')+1:word.find(')')] + word[word.find(')')+1:]
      new_words.append(new_word.strip())
      made_changes = True
    elif '/' in word:
      # Catches things like 'aglet/aiglet'
      # Add everything up to the slash and start at the next space
      if word.find(' ', word.find('/')) < 0:
        # Double check there is a space to find after the slash,
        # if not take none of it
        new_word = word[:word.find('/')]
        new_words.append(new_word.strip())
      else:
        new_word = word[:word.find('/')] + word[word.find(' ', word.find('/')):]
        new_words.append(new_word.strip())
      # Add everything but from the previous space to the slash
      new_word = word[:word.rfind(' ', 0, word.find('/'))+1] + word[word.find('/')+1:]
      new_words.append(new_word.strip())
      made_changes = True
    else:
      new_words.append(word)

  # Safety measure on the recursion
  depth += 1
  if depth > 10:
    print new_words
    return new_words

  # If we made changes, check if we need to make anymore
  if made_changes:
    return get_actual_words(new_words, depth)
  # Otherwise we are all done
  else:
    return new_words
