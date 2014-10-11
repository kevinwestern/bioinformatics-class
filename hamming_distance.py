from itertools import izip

def hamming_distance(str1, str2):
  return sum(a != b for a,b in izip(str1, str2))