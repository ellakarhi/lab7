import random

# variables
lower = "abcdefghijklmnopqrstuvwqxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "01223456789"
symbol = "!@#$%^&*()_+><.,[]{}\|"
password = ""

length = 4
lower_length = random.randint(0, length)

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

upper_length = length - lower_length
for i in range (upper_length):
  upper_rand = random.randint(0, len(upper)) 
  password = password + upper[upper_rand]

number_length = length - upper_length - lower_length

for i in range (number_length):
  