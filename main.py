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
