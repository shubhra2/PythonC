import collections

def check_equal_1(lst1, lst2):
    lst1.sort()
    print(lst1)
    lst2.sort()
    print(lst2)
    result = lst1 == lst2
    return result


def check_equal_2(lst1, lst2):
    cnt1 = collections.Counter(lst1)
    print(cnt1)
    cnt2 = collections.Counter(lst2)
    print(cnt2)
    result = cnt1 == cnt2
    return result

lst1 = [1, 2, 3, 4, 5, 6, 1, 2, 6, 6, 3]
lst2 = [2, 3, 4, 5, 1, 6, 6, 6, 2, 1, 3]

#status = check_equal_2(lst1, lst2)
status = check_equal_1(lst1, lst2)
if status == True:
    print("Two lists are equal")
else:
    print("Two lists are not equal")
