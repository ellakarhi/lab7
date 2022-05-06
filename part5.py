def getStr(message):
  while(True):
    temp = input(message)
    try:
      temp = int(temp)
      print("That is no the proper value")
    except:
      break
  return temp

def box(loop, name):
  length = len(name)
  for i in range(loop, length, 1):
    print(name[i], end = ' ')
    
  if loop > 0:
    for j in range(0, loop, 1):
      print(name[j], end = ' ')
  loop += 1
  if loop == length:
    print("")
    print("Your name has now been mixed up")
  else:
    print("")
    box(loop, name)

name = getStr("What name would you like to get mixed up: ")
box(0, name)


