lower = "abcdefghijklmnopqrstuvwqxyz"

#sentence = input("Enter a sentence: ")
#shift = int(input("Shift a number: "))

encrypted = ""
sentence = "ella is nice"
for letter in sentence.lower():
  if letter in lower:
    pos = lower.find(letter)
    encrypted = lower[pos+4]

else:
  encrypted = encrypted + letter

print (encrypted)