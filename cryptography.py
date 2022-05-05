lower = "abcdefghijklmnopqrstuvwqxyz"

def encryption():
  encrypted = ""
  sentence = input("What do you want to get encrypted: ")
  shift = int(input("How far shifted do you want it (positive numbers only): "))
  for letter in sentence.lower():
  
    if letter in lower:
      pos = lower.find(letter)
      encrypted = lower[(pos+shift) % len(lower)]

    else:
      encrypted = encrypted + letter
      
  print(encrypted)
  main()

def decryption():
  decrypted = ""
  sentence = input("What is your encrypted sentence: ")
  shift = int(input("What is it shifted by (negative numbers only): "))
  for letter in sentence.lower():
  
    if letter in lower:
      pos = lower.find(letter)
      decrypted = lower[(pos+shift) % len(lower)]

    else:
      decrypted = decrypted + letter
  print(decrypted)
  main()

def main():
  option = int(input("Do you want to encrypt (1), decrypt (2), or quit(3)?: "))
  if option == 1:
    encryption()
  if option == 2:
    decryption()
  else:
    exit()
  
main()