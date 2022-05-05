import random

# variables
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "01223456789"
symbol = "!@#$%^&*()_+><.,[]{}\|"

length = 10
lower_length = random.randint(0, length)
upper_length = random.randint(0, length-lower_length)
number_length = random.randint(0, length - upper_length - lower_length)
symbol_length = length - number_length - upper_length- lower_length

def making_password():
  """creates a random password but needs to be randomized again."""

  password = ""
  for i in range (lower_length):
    lower_rand = random.randint(0, len(lower)-1) 
    password = password + lower[lower_rand]
  
  for i in range (upper_length):
    upper_rand = random.randint(0, len(upper)-1) 
    password = password + upper[upper_rand]
  
  for i in range (number_length):
    number_rand = random.randint(0, len(number)-1)
    password = password + number[number_rand]
  
  for i in range (symbol_length):
    symbol_rand = random.randint(0, len(symbol)-1)
    password = password + symbol[symbol_rand]
  return password

def all_included():
  all_password = ""
  for i in range (1):
    lower_rand = random.randint(0, len(lower)-1) 
    all_password = all_password + lower[lower_rand]
  
  for i in range (1):
    upper_rand = random.randint(0, len(upper)-1) 
    all_password = all_password + upper[upper_rand]
  
  for i in range (1):
    number_rand = random.randint(0, len(number)-1)
    all_password = all_password + number[number_rand]
  
  for i in range (1):
    symbol_rand = random.randint(0, len(symbol)-1)
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
    password_rand = random.randint(0, len(last_password)-1)
    random_password = random_password + last_password[password_rand]
  print(random_password)
  
new_password()
print("ta da!")


'''
so, when you do random.randint, it considers BOTH numbers in the range.
So if I gave it 0 and 5, both 0 and 5 could be possible results from it.
The errors were happening when it was randomizing the max number (length of the character array) and when you are indexing an array, we always start at 0. SO, lets say it's the alphabet -- if the randint gives us 26, and we say lower[26], it's actually trying to get the 27th letter
of the alphabet, which doesn't exist. So to prevent that from happening in functions that use an inclusive range, we make sure to say (0, length-1) instead of (0, length). If that makes sense lol
'''

'''
Oh I also just noticed you had an extra letter in the 'lower' list, but I fixed it
'''
""" That does make sense. Thank you very much. I really appreciate it!"""

'''anytime :)'''