def combine_list(name, age):
  dct = {}
  for i in range(len(name)):
    nm = name[i]
    ag = age[i]
    dct[nm] = ag
            
  return dct

name = ['Ajay', 'Hardik', 'Bhavin', 'Dhaval', 'Premal', 'Raj']
age  = [20, 21, 19, 20, 22, 24]
dct = combine_list(name, age)
print(dct)