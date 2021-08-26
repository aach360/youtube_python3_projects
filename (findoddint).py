#given an array find one that appears an odd number of times.
def find_it(seq):
  for x in seq:
    a = seq.count(x) 
    if a%2 != 0:
      return x
      break