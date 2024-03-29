
# converts a number into a pattern
def number_to_pattern(number, k):
  if k == 1:
    return translate(number)
  return number_to_pattern(number / 4, k - 1) + translate(number % 4)



# translation table for hashes
def translate(symbol):
  table = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3,
    0: 'A',
    1: 'C',
    2: 'G',
    3: 'T'
  }
  return table[symbol]

# hashes a pattern
def pattern_to_number(pattern):
  if len(pattern) == 0:
    return 0
  return 4 * pattern_to_number(pattern[:-1]) + translate(pattern[-1])

# finds the reverse compelment of a pattern
def reverse_complement(text):
  complements = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
  }
  result = []
  for i in range(len(text)):
    result.append(complements[text[i:i+1]])
  result.reverse()
  return ''.join(str(x) for x in result)

# find the most frequent words of length k
def frequent_words(text, k):
  patterns = []
  count = []
  maxCount = 0
  for i in range((len(text) - k) + 1):
    pattern = text[i:i+k]
    count.insert(i, pattern_count(text, pattern))
    maxCount = max(maxCount, count[i])
  for i in range((len(text) - k) + 1):
    if count[i] == maxCount:
      patterns.append(text[i:i+k])
  return set(patterns)

# return an array of places pattern occured in text 
def pattern_count_indices(text, pattern):
  indicies = []
  for i in range(len(text) - len(pattern) + 1):
    if text[i: i+len(pattern)] == pattern:
      indicies.append(i)
  return indicies

# Return the number of times text occurs in pattern
def pattern_count(text, pattern):
  return len(pattern_count_indicestext, pattern)

def compute_frequency(text, k):
  frequency = []
  for i in range(pow(4, k)):
    frequency.append(0)
  for i in range((len(text) - k) + 1):
    number = pattern_to_number(text[i:i+k])
    frequency[number] = frequency[number] + 1
  return ','.join(str(x) for x in frequency)


def find_clump(text, k, clumpSize, minOccurences):
  locations = {}
  for i in range((len(text) - k) + 1):
    number = pattern_to_number(text[i:i+k])
    if number not in locations:
      locations[number] = []
    locations[number].append(i)
  result = []
  for key,v in locations.iteritems():
    if (len(v) < minOccurences):
      continue
    for i in range(0, len(v) - minOccurences + 1):
      if (v[i + minOccurences - 1] - v[i]):
        result.append(number_to_pattern(key, k))
  return len(set(result))



#print find_clump('TCCACCCCGGAGGAATATTCAATAAAGTTTGTAAAATGTCGCCGAACAAGGCTCGAGTCTTACACTGAATTAATGTCACATAAACTGGCCGGTAAAAACCCCTGCCATTGTCGGTTCGAAGTTCGAAGGAGCCGGTGTGTGCATCAATAATGCAGTTCAAAATACAATCTAGACGACGAAGGAAAACGCAGGTTCGTCCTGTAGGGGTAGACTCGTAAGGGAAAATGCACGCCTGATAACGATAATGCCACCGTGGCCATGCGTGAGTATGGATAGTGAAACTGGCGTACAGTCAGTGTTAAGACTCAGCAACATAGCTTTCCGAATCCCTGCCTAATCGTCTTCGCATGCGAAACGCGTATGCCGGATTAACTCTTTAAGATACTAACTCTAGTGCTGTTCGCGTCCACCCGTTCTGCTTCTCCAGAAATCGACTGACGACCATAGGAGACTACTCTAAGCACGGCCAGCAATCATTATACGCAAATCGCTAAACGGAGTTCGCCCAGATCGGCCACTGAAAGGGAAATGTAATCTGTGGAATCCTTAAACGGAGGAGTCACCTCCCGCTGTTGACTCGCTTTCATACACACGATAATTTCCCGTATCCGGGACTTCAATCCCGAGCGCGATTTACTCGGAGATTGGAGCAACCCCAGAATGTAGCACATATTGTCGAGGGGGGACGATACACTTTCGGAATTTTTGGCTTCAAGTCGACTCGCATAGCAGGACACGGCGGAATATAAGTTTCCGTCAAGGTTTTAAAATACATGAGGGGGGGACTTTTGCACAACCGGTTTAAGTGCACTTATGCTATTAATTTATAGCATTGAAAGATCGACAGCAGCCCAGTCTCCCACTTTCTCTTCAATGCTGGATACGGCTCCTAATAGGCCTCCCGGATTGGTCGCCAATCTAACATAAGCCGACTCCCTGAACACTAGTCCACGCGGCGATTGGCGGTTACGCATTGTTTCTGACTCGTTATTCACAATGATTCGGTCTAAGACATTACTGAGTTTGGACTAACGACTCCGGTTTGCTCCTTCCGCTCCCGATTGCAATCGCTGGTGCTAAAGTACGCTGGCATGCAATTTGCAGGACGCTAATGCAGAGTGAAGTCAGCAGCCCTGGAAGAATTTCAGAGCTCCTGCGCAGGTAGTCGTTGCGCTAGCCTCGAGGCGACAGAGCTCTCCACTAATTAGTGAGGTGCGCCTTCCCTTACCTAATGGTTTTGGGTAATTATGTGTAGTGCTACAGACGTCACCCTGGCGGGATACACTCCTACAAGAAGCTAAACTGGATAAATTAGTGGGCGCTGAAGAGAGCTGATTTGTGGAATACCGTTGTCAACTGCGGCGTAACCTCAGCGTTGGAGAGCTTATAATCCTATCTTGGGAGCATCTGGACTAGACGGCTAGCTTCTTGTCGAGAACGAACGTAGTAGCTATGCTTACGGAATTGGGTGTAGGGATGAACGTGATATTCCTGCCACCGACAGGAACGTCCCCATCCCAGAGAAGACTCGGACTTCATTATGTTACTCCCGATTTGTACCCCTAGATCCTATATTAGCTATTAGCCTCTCCAGACCGGGGTTCCGAAATCCTATATTAGCAAGGAAATCCTATATTAGCGCTCCTATATTAGCCCACTCTCCTATATTAGCCATGTTCCTATATTAGCTTAGATATCTTGCTGCTTAATCCTATATTAGCCTCGATATTTCCTCCTATCCTATATTAGCCAGTGGCAGTCGTCATCCGATATATGACCACATGCCCATCCGGCATCGCACTCTCCTTCCTATATTAGTCCTATATTAGCTAGCCATCCTATATTAGCCTATACAGATGGGCCCGTCCTCCTCCTATATTATCTCCTATATTAGCAGCATATCCTATATTAGCTGGGCATGGGGAATGATAATGTTTTCCATGCGCGGCCATGCGCGGCGCGGGCGTGGAGGTCCTTCCTTCCTATATTCCATGCGCGGTAATGCCATTCCTTCCATGCGCGTTCCATGCTTCCATGCGCGGTCGCAGTTCCATGCGCGGTCCTATATTAGCCGGTTCCATGCGCGGTTCGGGTCCTATATTTCCATGCGCGGCTACTACTTTCCATGCGCGGTTTAACACCCAATTAGTCGCTACTCGTTTCCATGCGCGGGACTGTCTTACAATTTAGTACGCGGTCGTACATCATGTATTCTTAGATTCCATGCGCGGCGCGGATTCCATGCGCGGATGCGCGGTAACTTCCATGCGCGGTTCCATTTCCATGCGCGGTGCGCGGGCCGCCTCCATCCGTGGCTCCTTCCATGCGCGGATTCCATGCGCGGCATGCGCGGTAGCCGGGTGGGTAAGACGCGCTCACGCCCTTGAAATTCCATGCGCGGGGCACGCCTTGTCTTCCATGCGCGGAAATACATTTCCATGCGCGGAGCTTCCATGCGCGGCTCTACAAAGGGCATCCATGCGCGGCGGACGTTAATTCCATGCGCGGTCCCTACAAAGGGCATACAAAGGGCAGCGAGTTGCCGGCCTATTTGGCATCTCGCCATGATCTCGCTACAAAGGGCAACAACTACAAAGGGCAACAGCCTACAACTACAAAGGGCATGGGAAGCGCTACTCGAATCAGTAGGTAAATTCTACAAAGGGCACTACAAAGGGCACACGCTACAAAGGGCAAGATATAGAACGCTACAAAGGGCCGCTGTCGGCGCCTGTCGGCGCCCTGGACGCCGGTCGCGCTGTCGCGCTCGCTGTCGGCGCAGTTTTCCGCTGTCGGCGCGCTGTCGGCGCTCGGCGCGCGCCTACAAAGGGCCCGCTGTCGCGCTGTCGGCGCCCGCCGCTGTCGGCGCCTCCTACAAAGGGCAGGAACGGTATCGGGAAAAAATTTCTGGCGCTGTCGGCCGCTGTCGGCGCCGCTGTCGGCGCCCGCTGTCGGCGCGCACGGTGACGCTGTCGGCGCTACACGCTGTCGGCGCCTACAAAGGGCAGGGCAATAATCTTGGAGCTACAAAGGGCACAAAAGGGCACTGTTGAGGCCTTCAAAAAGGCAGCGCTGTCGCGCTGTCGGCGCGATATATTTTGGAAATACGCGTCTAGGACTCGCTGTCGGCGCACGCGCTGTCCGCTGTCGGCGCACTTTAATCGCTGTCGGCGCCGCTGTCGGCGCGGCCATGAACATGCAAGTATTACCGCTGTCGGCGCGGCGCTGTCGGCGCCGCGCTGTCGGCGCGCTGTCGGCGCGGTTCGACGCAGGCCAACTAATGCAGGCCAAGCTGAGACCTGGTGTAAGGCTTACGCTCAATTCTAAGCGGCCATGCTCCGATTTGCAGAACCCGGTTTATCTAACGAACGAGAGGAGACAAGCTGTTATAACGTACTAGCGAACCTTACAGCCGCAACACCAACAAGTCGACGGAAAAAATTGAACCTCTCCCCTGGTTCTTTCAGCTGAGGATATCGGCTACTACTTTGGCCCTTAAATGTTTCACGGCTCGCCGACAAAAGACATAGATATAGAGCCGGGAGAGCCGGGGGGGGGGGGCGGGGGGGTCCAGAGCCGGGGGGGGGGGGGAGCTCAGAGCCGGGGGGAAGTGCGGCATTCTGCCCAACTTTGGTTCAGTCATATAGAAGAGCCGGGGGGAGCCGGGGGGGGAACCAATCTTCACTGCAGAGCCGGGGGGCTGTAGAGCCGGGGGGGGGCTCGATATAGAGAGCCGGGGGGTCCCATTCCCGCCGAATGTGGATTCCCCGAGAGCCGGGGGGCTAACCCTAGAGCCGGGGGAGAGCCGGGGGGCTCACAATATAGAGAGAGCCGGGGGGGGGCTGAAGGCTCGAGAGAGCCGGGGGGGGGGGGACCAGAGCCGGGGGGAGAGCAGAGAGCCGGGGGGATCTTGGATTCCAGAGCCGGGGGGGCTGAATTTACAGAATTAATAGAGCCGGGGGGTCGGTTATCGTTGTGTCGGCGTTATCATCTATAGAGCCGGGGGGCAACATAGAGCCGGGGGGGGGTGAGACAATATCAGACGTACGTTATACGGTTGAAACAGAGAGCCGGGGGGATCCCTCCAGAAGAGCCGGGGGGCTTATAAAACTCGTGGAGTGATGTTTAGTCAGGTCCTGTCCTACAGAAACGTATAAAGTTTACCACAGGAACGAATGGCGAGTCCTATTGACCATTATAGCCACGCGCCCCTTGAATAGGTCTTCCATTCTCAGTGGTCAGACCATAAATATAGTAGAGTAAATATAGTAAATATAGTAGCCTCCAGTATAAATATAGTAGCTAAATATAGTAGTAGGTAGGTTCGGCACTATTATTTTCTCGTAAATATAGTAGAGTTTACCTGCGTTGTAACTAAATATAGTAGTATAGTAGATAGTCACCTATTACTCGCACCGCGGCCTCCACTAACTGGCCCAGCTCGTAAATATAGTATAAATATAGTAGTAACCTAAATATAGTAGTAGTAGTTCTCCTAAATATAGTAGGAACATCTAAGCGGGGTGCGAGATAAATATAGTAGAACGACATTGCAATTCCGCGGTAAATATAGTAGTCAGTCCCTTATAAATATAGTAGCAGTAACTCGATTGGCGACCACTAAATATAGTAGGTGTAGTGCGCGTGAGCCTGCATCTCATTATAAATATAGTAGATATAGTAGTTATTGAGAGACTTCGACGTTTTGCATTAAATTAAATATAGTAGTAGTAATAAATATAAATATAGTAGCAAGGGGGCGGTGTTAAATTAAATATAGTAGAACATTAAATATAGTAGTGTCTACGGCCAAAAAAATTAAATATAGTAGAAATATAGTAGGCGCTCGTACGGGGTGGGCAGCCGTTCCTCGGTGCCCTATCCTGGGTAGTACTCTCAGGGATGGCAAGTATAATTTCCCCTGTTACTTGTATCGACTCACATCGGTTTCCTGAGATCTCTAGCGGTACTTGGACGGGTTTGCACGGGTTTGCTAGAAGCCGTCCACACGGGGTTAGCAGACCCTCCATCCATAACCTACGGGTTTGCTATTTGCTAATGTACGGGTTTGCTAACGGGTTTGACGGGTTTGCACGGGTTTGCTACAGACACGGGTTACGGGTTTGCTACTAATCTGGGGTTTCTTCTAGCGCTGTCGGGTTCTCGGTCGTGTCAAGTTGACGGGTTTGCTACCATCTGACGGGTTTGCTAGGAGGGTTTCTAAGACGGGTTTGCTAATTTACCCCCATCGTGCACCCACGGGTTTGCTATGCACGACGGGTTTGCTAGACGGGTTTGCTATGCCAGACGGGTTTGCTAATTAGGCAACGGGTTTGCTACGACTTTTCTTGACGGGTTTGCTACAGTCAGTGTAGAAAAACGGGTTTGCTAGAACGGGTTTGCTAGCTACGGGTTTGCTAAGATTGACTCAACGGGTTTGCTAACGGGTTTGCTACGGGTTTGCTAAGACGGGTTTGCTATGCTACACCGTCGGGACGGGTTTGCTAGCACGCGATGCCACGGGTTTGCTATTGCTAAAATAAGGAGAGTGTACGTGTGACAGAAAACTCTATATCTGGATTTATGACCACACACCTATCGGCCTGTATCGTTGAGTGCACCTGCCCGCGCCGGTCCATCTGGCTTAAGCCCAGTGGCCAACTATGGGACGGCATTAATCCCATAGTAAGCTTCGCATTATGAGGTGAGTTAATCAGAGGCGAATAGAGTCTGTCCCCGTGCCTATTGGTCCGCTATCCGATTACGACTGGATCCCGCACCTTCCACCCACACGCCATGAGAGGAGTTGCATCTCGAGTTGCATCTCGAGTTGCATCTCGCAGTTGCATCTCGCGAGTTGCAGTTGCATCTCGCGGTTGCAAGTTGCATCTCGCGTCACAGATTCACCAGTTGCATCTCGTAGTTGCATCTCGGGCCAAGTAGTTGCATCTCGATTCCTACAACGGAGTTAAGTTAGTTGCATCTCGCTAAGTTGCATCTCGATCTCGTTGAGCAGTTGCATCTCGGAGTGTACCAATGGACTCCGCGTTAGGCCGCTGGAGTTGCATCTCGATCTGTTCATGCAACATCGATAAAGTTGCATCTCGAGAGTTGTTAGTTGCTAAAATGTCACGAGTTGCATCTCGGGTAGTGAATGTTTAATTGTGAGTGTAGTTGCATCTCGCACAGTTGAGTTGCATCTCGAGTTGCAGTTGCATCTCGTGAGTTGCATCTCGTATTAACCGGAGTTGCATCTCGGCATCTCGGGACCCCAGTTGCATCTCGACGGAAAAGAATGAAGTTGCATCTCGCGTTCTCAGAGCCTTGTGAAGTTGCATCTCGCGCGCACAGTTGCATCTCGACACAAACCTCAAATGAGCGAGTTGCATCTCGTGAGTTACCATAGCATCCCCGTTGAAGCGTGCTGGTATCCTTCTCGCTCTACCTCCTGCGGAGAAATGGGTATCAGAATGACGTCGTCTCTTTAACTATCGATCACTCTAAAGGCCATGGTTTTCACCACAAGCGCTTCTGTTCCCTGAAGGTCTGGCTTAACAATGCTTTTCCCGCTTCTACGTCAGCGACACAAAATCCTATGAAGATCGCTGAACGTCGCTTCAAATGCTAATTATTAACTCCCGCATATAGGGATTCCTCTCGACATAGCTGACGTCCAGTTAACGCAGTAGCTATCTCTAGATGTGCATAAGGACCATTTCCCTGGAACCGACTAGGGGGCTCAATGCCAGGACTCCTGATAACCGACAGTAGAGAGCTACAACAGCCCCGCCCTCTAACTGGAGCGACATGGGGTCACAAGGGACAGGATTATGATGATAGTTGGAGACGGACCCAAACCGGCGGGACCTGTAAGGATTGGTTCCTTTCTGCCGGTGCTCAACTCTATAACGAGGTGACAACGTGCATTTCCCACGAGTTGTGCCCATACCCTTGTTTAACACTTGGGCGGGACTATGGAAAGTAGGGGGCAACTAGAGGCTTCGAAGGCTTATTATAGCAATTTAGCCCTGGAGGCAAAGTGCACGGGGTTTACGGTTTACGCCCTTATTCAGTGAATAAGAAATGACGGCACGGGGTTTACCTCGTTGACCCTACGCACGGGGTCACGGGGTTTACTGTTCGCCACGGGGTTTACCCACTTCACGGGGTTTACTCACGGGGTTTACCCACGGGCACGGGGTTTACTTACCCACGGCACGGGGTTTACGGTTTACTACACACTGCATTTCCATTGTGCTGCCTTTCCATTGTGCCATTGTGCCTCTTGAGCACGGGGTTTCCATTGTGCATTGTGCCATTGTGCGGTTTCCATTGTGCCCCCATCTACACGTTTCTTTCCATTGTGCCCATTGTGCTTTTTTTCCATTGTGCCGTTTCCATTGTTTCCATTGTGCACATTTCCATTGTGCTTACAAGTCCGGTTCCAGCACGGGGTTTACACGGGTTTACTAACCGTTTCCATTGTGCTTCCATTGTGCCTACGGTAGCACGTTTCCATTGTGCGTTTCCATTGTGCGGTTTACGCATGCACTCCCACGGGGTTTACGCCCGTCGCTGTTTCCATTGTGCTGCAGAGGTCCTCATTTCCATTGTGCTTTCCATTGTGCTTTTCCTTTCCATTGTGCTTTCCATTGTGCTTGTACAAGCTTGAACCTTACAAGCTTGAACAGCTTGAACCTTTCCATTACAAGCTTGAACTTGACACAAGCTTGAACACAAGCTTGAACATGGATCTAGTTTCCATTGTGCTGTTTTTCCATTGTGACAAGCTTGAACAAGCTTGAACAAGACAAGCTTGAACTACAAGCTTGAACCCGTCGTCAAGGCGGCTTCCGTCGAAACAAGCTTGAACAACTGATAACAAGCTTGAACGAACTTAAGATGACCGGAACACTACAAGCTTGAACGCTTGAACGGCTTAGTCTAACACAGCTACCTTTCTTAATCTACAATGCACAAGCTTGAACTGGCCACTGCCGAACAAGCTTGAACCACAAGCTTGAACGATAGGACCTCGTTCACAAGCTTGAACTGTCCTTTATTCGGCATTAACATAGGCGGGGACAAGCTTGAACAGATCATACTTACAAGCTTGAACAACTAAATGCAACAAGCTTGAACCAACAAGCTTGAACAGTCCAAACAAGCTTGAACACAAGCTTGAACCTTGAACATGCCTTCCAATTTCTCCCATACTCCGAAGACTCGCCTATGAGTAGCCTGCGTCCTCGCCTACGTTCCTGTTTGGCTTTGCGCAAGAGGTCAAGGTGATAAGGGACTTGAAACGTTCCAATCTATACGGGCTCACCTATAACTTATTACTGCCCACGATTCCGTAACTTATGTTTAACGTTCAGAATTTACATGCAAGATACATCCAACATCCGGCGATGGTGAGTCCATGCTATCAGAACTGCATGACCACGTACTGGATCCGGCGCTGTTGTATTATTTTCAAGTGCCCCAGACAATGACTTCGATACCGACATCAGTAGCTTAACCTGTGAATACGAGGATTATGGATTAGCAGGCGATTGTCCACATGAAAAGGTGAGACAGCTTAAGCCAGGGCGTACTGCCCACACTTTATGGCGCGCCAGGCGGTACTGAGCTGATATGGTCTTGGAGGTAACATATGCCGAGACTCATAATAGGGGTACCGCGGGATACACAGGCCTAGGCAATGTGGCAATAAACAATGTACACGATGAATGTCACTAGAGCGTGCTCGTGCGCAGCGCGTGGGGTATAGCCCACGTATGGTCGTAGGTAGACGGTGTCAACACTAAAACCATTACGAACGCGGTGACAATCTAAGTTCCGTTGGTGACGTTCGTTTACTTGATTAATTCATCCAGCGTGTCACACTAATGAGGATTTTATATGCCTTACCGGTCGATTAGATGA', 12, 598, 19)

with open('ecoli.txt', 'r') as f:
  genome = f.read()
  print find_clump(genome, 9, 500, 3)
