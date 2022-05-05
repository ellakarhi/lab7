lower      = "abcdefghijklmnopqrstuvwxyz"

def encryption ():
  encrypted = ""
  sentence = input("Type in a sentence: ")
  shift = int(input("What is the shift number (positive only)? "))
  
  for letter in sentence.lower():
    
    if letter in lower:
      pos = lower.find(letter)
      encrypted = encrypted + lower[(pos+shift) % len(lower)]
    else:
      encrypted = encrypted + letter

  print (encrypted)
  main()

def decryption ():
  decrypted  = ""
  sentence = input("Type in your encrypted sentence: ")
  shift = int(input("What is the shift number (negative only)? "))
  
  for letter in sentence.lower():
    
    if letter in lower:
      pos = lower.find(letter)
      decrypted = decrypted + lower[(pos+shift) % len(lower)]
    else:
      decrypted = decrypted + letter

  print (decrypted)
  main()

def main():
  option = int(input("Did you want to encrypt (1) or decrypt (2) or quit (3)? "))
  
  if option == 1:
    encryption()
  elif option == 2:
    decryption()
  else:
    exit()

main()