import random

# variables
lower = "abcdefghijklmnopqrstuvwqxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "01223456789"
symbol = "!@#$%^&*()_+><.,[]{}\|"
password = ""
#random_password = ""

length = 10
lower_length = random.randint(0, length)
upper_length = random.randint(0, length-lower_length)
number_length = random.randint(0, length - upper_length - lower_length)
symbol_length = length - number_length - upper_length- lower_length

def making_password():
  """creates a random password but needs to be randomized again."""

  password = ""
  for i in range (lower_length):
    lower_rand = random.randint(0, len(lower)) 
    password = password + lower[lower_rand]
  
  for i in range (upper_length):
    upper_rand = random.randint(0, len(upper)) 
    password = password + upper[upper_rand]
  
  for i in range (number_length):
    number_rand = random.randint(0, len(number))
    password = password + number[number_rand]
  
  for i in range (symbol_length):
    symbol_rand = random.randint(0, len(symbol))
    password = password + symbol[symbol_rand]
  return password

def all_included():
  all_password = ""
  for i in range (1):
    lower_rand = random.randint(0, len(lower)) 
    all_password = all_password + lower[lower_rand]
  
  for i in range (1):
    upper_rand = random.randint(0, len(upper)) 
    all_password = all_password + upper[upper_rand]
  
  for i in range (1):
    number_rand = random.randint(0, len(number))
    all_password = all_password + number[number_rand]
  
  for i in range (1):
    symbol_rand = random.randint(0, len(symbol))
    all_password = all_password + symbol[symbol_rand]
  return all_password 

  
def new_password():
  """randomizes the original password so the the same variables aren't beside each other."""
  all_password = all_included()
  password = making_password()
  last_password = all_password + password
  random_password = ""
  p = len(last_password)
  
  for i in range(p):
    password_rand = random.randint(0, len(last_password))
    random_password = random_password + random_password[password_rand]
  print(random_password)
  
new_password()