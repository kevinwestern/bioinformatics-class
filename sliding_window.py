

def sliding_window(text, windowSize):
  for i in range(0, len(text) - windowSize + 1):
    yield text[i:i + windowSize]