def substr():
  
  s = str(input("Enter a word: "))
  i = int(input("Enter an index: "))
  length = int(input("Enter a length: "))
  
  
  assert isinstance(s, str), "s must be a string"
  assert isinstance(i, int), "i must be an integer"
  assert isinstance(length, int), "length must be an integer"
  
  x = len(s)
  if i < 0:
    print (s[0:0])
  if length <= 0:
    print (s[0:0])
  if length > x:
    print (s[i:len(s)])
  else:
    print (s[i:i + length])
  
  
substr()