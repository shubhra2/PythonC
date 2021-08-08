import collections
string = 'Hi How are you?'
cntDict = {}
for char in string:
  if char not in cntDict:
    cntDict[char] = 1
  else:
    cntDict[char] += 1
print(cntDict)

#string = 'Hi How are you?'
cntDict = collections.Counter(string)
print(cntDict)
