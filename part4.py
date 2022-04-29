name = input("Enter a name: ")
name_length = len(name)


for k in range (name_length) :
  line = ""

  for i in range (name_length):
    z = k + i
    
    if (z >= name_length):
      z = z % name_length
      
    if (i == 0):
      line = line + name[z]
    else:
      line = line + "\t" + name [z]

  
  print (line)