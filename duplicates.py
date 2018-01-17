def duplicate_count(text):
    count, dups = {}, 0
    for s in text:
      if s.lower() in count:
        count[s.lower()] += 1
      else:
        count[s.lower()] = 1
    for key in count:
      if count[key] > 1:
        dups+=1
    return dups