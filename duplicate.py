def duplicate(lst):
  dup = []
  while(len(lst) > 0):
    elem = lst.pop()
    if elem in lst:
      print(elem, ' is duplicate')
      if elem not in dup:
        dup.append(elem)
  return dup

lst = [1,2,3,4,4,3,3,4, 5, 6, 7, 6]
dup = duplicate(lst)
print('Duplicate elements in list are : ',dup)