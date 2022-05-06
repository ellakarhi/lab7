def substr():
  
  s = str(input("Enter a word: "))
  i = int(input("Enter an index: "))
  length = int(input("Enter a length: "))
  
  assert isinstance(s, str), "s must be a string"
  assert isinstance(i, int), "i must be an integer"
  assert isinstance(length, int), "length must be an integer"
  
  subs = ""
  x = len(s)
  
  if i < 0:
    return
  if length <= 0:
    return
  if length > x:
    for i in range (i, len(s)):
      subs = subs + s[i] 
      print(subs)
    #print (s[i:len(s)])
  else:
    for i in range (i, length + i -1):
      subs = subs + s[i] 
      print(subs)


substr()