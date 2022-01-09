name = input("Name: ")

print(f"Welcome to my computer quiz!")

play = input(f"Would you like to play a game {name}? ")

if play != "yes":
    quit()

print("Great! Let's play a game :) ")

# Q1
answer = input("What does CPU stand for? ")
if answer == "central processing unit":
  print("Correct!")
else:
  print("Dang foo, you wrong.")


# Q2
answer = input("What does GPU stand for? ")
if answer == "graphic processing unit":
  print("Correct!")
else:
  print("Dang foo, you wrong.")


# Q3
answer = input("What does RAM stand for? ")
if answer == "Random Access Memory":
  print("Correct!")
else:
  print("Dang foo, you wrong.")


# Q4
answer = input("What does PSU stand for? ")
if answer == "Power Supply":
  print("Correct!")
else:
  print("Dang foo, you wrong.")

