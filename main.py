print("Welcome to the rollercoaster!")
print()
height = int(input("What is your height in cm? "))
print()

#Checking if the customer can ride the rollercoaster
if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5")
  elif age <= 18:
    print("Please pay $7")
  else:
    print("Please pay $10")
else:
  print("Sorry you have to grow taller before you can ride")