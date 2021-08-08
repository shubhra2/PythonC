
def test_location(cards, query, mid):
  mid_number = cards[mid]
  print("mid: {}, mid_number: {}".format(mid, mid_number))
  if mid_number == query:
      if mid-1 >= 0 and cards[mid-1] == query:
          return 'left'
      else:
          return 'found'
  elif mid_number < query:
      return 'left'
  else:
      return 'right'

def locate_card(cards, query):
  lo, hi = 0, len(cards)-1

  while lo <= hi:
      print("lo: {}, hi: {}".format(lo, hi))
      mid = (lo+hi)//2
      result = test_location(cards, query, mid)

      if result == 'found':
          return mid
      elif result == 'left':
          hi = mid-1
      elif result == 'right':
          lo = mid+1
  return -1
test = {
    'input': {
        'cards': list(range(1000000000, 0, -1)),
        'query': 2
    },
    'output': 9999998
}
out = locate_card(**test['input'])
print(out)