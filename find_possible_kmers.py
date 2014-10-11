
from hamming_distance import hamming_distance
from sliding_window import sliding_window
from itertools import permutations

def find_all_unique_kmers(text, size):
  return list(window for window in sliding_window(text, size))

# the most popular one does not have to be in the text!
def find_possible_kmers(text, kmerSize, maxMismatches):
  result = {}
  for permutation in permutations('ACGT', kmerSize):
    print permutation


find_possible_kmers('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1)
