# STEP 1: Learn the Syntax of simple function
def function_name():
  Do this
  Then do this
  Finally do this
function_name()

# STEP 2: Learn how the syntax works 
1. def meaning defining 
2. everything after the colon that is intented after (): belongs to the function
3. to trigger the function or "call" the function 

# STEP 3: Learn Functions with a Input
def function_name(something):
  Do this with something
  Then do this
  Finally do this
function_name()

something in the paraenthesis is called PARAMETER 
something (parameter) = 123 (argument)

# STEP 4: LEARN Function with multiple inputs
def function_name(something1, something2):
  Do this with something
  Then do this
  Finally do this
function_name(123, ABC)

# STEP 5 Positional vs. Keyword Arguments 
def function_name(something1 = 123, something2 = ABC):
  Do this with something
  Then do this
  Finally do this
function_name()

STEP 6 PRACTICE THESE EXCERCISES 

# Area Calc
import math
def paint_calc(height, width, cover):
  area = height * width
  number_of_cans = math.ceil(area / cover)
  print(f"You will need {number_of_cans} can of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)


## PRIME NUMBER CHECKER
n = int(input("Check this number: "))

def prime_checker(number):
  is_prime = True
  for i in range(2,number-1):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print(f"{number} is Prime")
  else:
    print(f"{number} is Not a Prime")

prime_checker(number = n)

## Ceaser Ghost
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    # square brackets [] to access data in the list
    cipher_text += new_letter
  print(f"{cipher_text}")


def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter2 in cipher_text:
    position = alphabet.index(letter2)
    new_position = position - shift_amount
    new_letter = alphabet[new_position]
    plain_text += new_letter
  print(f"{plain_text}")
    
  

if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text = text, shift_amount = shift)

