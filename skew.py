with open('genome.txt', 'r') as f:
  genome = f.read()

  minimums = []
  minimum = 0
  total = 0
  for i in range(0, len(genome)):
    if total == minimum:
      minimums.append(i)
    if total < minimum:
      minimum = total
      minimums = [i]
    nuc = genome[i:i+1] 
    if nuc == 'G':
      total = total + 1
    if nuc == 'C':
      total = total -1
  print ' '.join(str(x) for x in minimums)
