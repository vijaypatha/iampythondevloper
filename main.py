#1. Create a greeting for your program.
print("Welcome to the Brand Name Generator")
#2. Ask the user for the city that they grew up in.
city_name = print(input("What is the name of city that you grew up in?"))
#3. Ask the user for the name of a pet.
pet_name = print(input("What is the name of your pet?"))
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city_name +"" + pet_name)

####### TIP Calculator 
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n"))
split = float(input("How many people to split the bill?\n"))
perc = float(input("What percentage tip would you like to give? 10, 12 , or 15?\n"))
result = round(( bill / split ) + (( bill / split ) * (perc / 100 )),2)

print("Each person should pay: " + str(result))
print(f"each person should pay: {result}")

####### Leap year
if year % 4 != 0:
  print("Not a Leap year")
elif year % 100 != 0:
  print("leap")
elif year % 400 == 0:
  print("leap")
else:
  print('not leap')

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 ==0:
#       print("leap")
#     else:
#       print("not leap")
#   else:
#     print("Leap")
# else:
#   print("Not leap")


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("You are at a crossroad, where do you want to go? Do you want to go left or right?\n").lower()


if choice1 == "left":
  choice2 = input("You magincally arriaved at a lake. There is an island in the middle of the lake. Do you want to swim or wait for a boat? Type swim or wait\n").lower()
  if choice2 == "wait":
    choice3 = input("Good that you waited for the boat. Now you entered the island and you have a chooise for one of the three doors: Blue or Red or yellow\n").lower()
    if choice3 == "red":
      print("The red door is a opening to a volcano and your feel into it.")
    elif choice3 == "blue":
      print("Blue Door opens to a jungles of Africa and you are eaten by beasts")
    else:
      print("You have choose wisely and you win")
  else:
    print("Attacked by slimy demon trouts. Game Over. remember to choose the right!")
else:
  print("Oops you fell right away into a big hole; game over")


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
