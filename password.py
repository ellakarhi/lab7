import random

# variables
lower = "abcdefghijklmnopqrstuvwqxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "01223456789"
symbol = "!@#$%^&*()_+><.,[]{}\|"
password = ""

length = 4
lower_length = random.randint(0, length)
upper_length = ramdom.randint(0, length-lower_length)
number_length = random.randint(0, length - upper_length - lower_length)
symbol_length = length - number_length - upper_length- lower_length

def generate_lower():
  return random.randint(0,len(lower))
  
for i in range (length):
  lower_rand = random.randint(0, len(lower)) 
  password = password + lower[lower_rand]
  print (password)
for i in range (lower_length):
  lower_rand = random.randint(0, len(lower)) 
  password = password + lower[lower_rand]
  print (password)

for i in range (upper_length):
  upper_rand = random.randint(0, len(upper)) 
  password = password + upper[upper_rand]

for i in range (number_length):
  number_rand = random.randint(0, len(number))
  password = password + number[number_rand]

for i in range (symbol_length):
  number_rand = random.randint(0, len(number))
  password = password + number[number_rand]
