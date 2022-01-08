# practice types of string concatination
name = "Napoleon"

print("have you seen " + name + "?")
print(f"do you know anyone named {name}?")
print("I want to name my new dog {}".format(name))

# variable initializations
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

# string variable holding other variables
madLib = f"Computer programming is so {adj}! It makes me so excited\
  all the time because I love to {verb1}. Stay hydrated and {verb2}\
  like you are a {famous_person}! "


# print/run madLib
print(madLib)