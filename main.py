print("Welcome to the rollercoaster!")
print()
height = int(input("What is your height in cm? "))
print()
bill = 0
#Checking if the customer can ride the rollercoaster
if height >= 120:
  print("\nYou can ride the rollercoaster")
  age = int(input("\nWhat is your age? "))
  if age < 12:
    bill = 5
    print("\nPlease pay $5")
  elif age <= 18:
    bill = 7
    print("\nPlease pay $7")
  elif age >= 45 and age <=55:
    print("\nYour age range qualify you to have a free ride on us. ENJOY")
  else:
    bill = 12
    print("\nAdult ride is $12")
  want_photo = input("\nDo you want photo,enter Y or N? ")
  if want_photo == "Y":
    bill += 3
  print("\n=======================================")
  print(f"\nYour final bill is ${bill}")

else:
  print("\nSorry you have to grow taller before you can ride")