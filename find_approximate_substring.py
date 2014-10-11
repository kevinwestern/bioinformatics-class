import hamming_distance

def find_approximate_substring(text, substring, max_mismatches):
  positions = []
  for i in range(len(text) - len(substring) + 1):
    window = text[i:i + len(substring)]
    if (hamming_distance.hamming_distance(window, substring) <= max_mismatches):
      positions.append(i)
  return positions
print len(find_approximate_substring('GAGGGCAATGTTTATGGTGTCAGCTGATGATGTAGGGTACCCCATAAGGTTTTGTTGGTATTCGACCCTGGAGGTAGTGGCCGAAGCACTTGACTGAACGCTATGCGCCTGTAACGGCGGACCTGTAACAGAGCGCACGCCAACAACGTTGTGCGACAGTTTTTTACTGAAGTTTATGCCCATCGCTGTGTACACGCCAGTCACAGACAACACGCGCAGCGTAGCTGCCAATGAACCCAGATTGGCGCGCTTTGCATGTGCTCACAGTACTCTGGAACTTTATATTCACCGATGTCCATTGGAAATGGCTGTTCAATATAGAGGCATCCGAAAGCAGCTTCCAC', 'CGGCGG', 3))