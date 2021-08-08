def unique(lst):
  dct_count = {}
  unq = []
  for elem in lst:
    if elem not in dct_count:
      dct_count[elem] = 1
    else:
      dct_count[elem] += 1

  for elem, cnt in dct_count.items():
    if cnt == 1:
      unq.append(elem)
  return unq

lst = [1,2,3,4,4,3,3, 5, 6, 7, 7]
unq = unique(lst)
print('UNique elements in list {} are {}'.format(lst,unq))