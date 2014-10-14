
from hamming_distance import hamming_distance
from sliding_window import sliding_window
from itertools import permutations

def find_all_unique_kmers(text, size):
  return list(window for window in sliding_window(text, size))

def mutateIndex(text, index):
  result = []
  mutation = ''
  for nuc in ['A', 'C', 'G', 'T']:
    if index == 0:
      mutation = nuc + text[1:]
    elif index == len(text) - 1:
      mutation = text[:-1] + nuc
    else:
      mutation = text[0:index] + nuc + text[index+1:]
    if mutation != text:
      result.append(mutation)
  return result

def mutateColumns(text):
  mutations = []
  for i in range(0, len(text)):
    mutations += mutateIndex(text, i)
  return mutations


def populate_similar(text, numMaxDifferences, neighborGraph):
  if text in neighborGraph:
    return neighborGraph
  neighborGraph[text] = {}
  variations = [text]
  previousMutations = []
  for i in range(1, numMaxDifferences + 1):
    length = len(variations)
    mutations = []
    for j in range(0, length):
      for mutation in [m for m in mutateColumns(variations[j])]:
        if mutation in neighborGraph[text]:
          continue
        neighborGraph[text][mutation] = i
        if mutation not in neighborGraph:
          neighborGraph[mutation] = {}
        neighborGraph[mutation][text] = i
        variations.append(mutation)
        mutations.append(mutation)
    previousMutations.append(mutations)

    # Tell neighbors about each other and previous neighbors
    for index in (len(previousMutations) - 1, -1, -1):
      steps = (len(previousMutations) - 1) - index
      lastMutations = previousMutations[index]
      for mutation in mutations:
        for lastMutation in lastMutations:
          if lastMutation not in neighborGraph[mutation]:
            neighborGraph[mutation] = steps
          if mutation not in neighborGraph[lastMutation]:
            neighborGraph[lastMutation] = steps
  return neighborGraph

print populate_similar('AAA', 2, {})


# the most popular one does not have to be in the text!
def find_possible_kmers(text, kmerSize, maxMismatches):
  result = {}
  for permutation in permutations('ACGT', kmerSize):
    print permutation



#find_possible_kmers('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1)
