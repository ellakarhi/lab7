def substr(s, i, length):

  subs = ""
  
  for i in range (i, length + i):
    subs = subs + s[i]
    
  print(subs)

substr("wordhjhh", 2, 4)