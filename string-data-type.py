"""
Your module description
"""
myString = "This is a string."
print(myString)

print(type(myString))

print(myString + " is of the data type " + str(type(myString)))


firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)


print('------------')

name = input("What is your name? ")
age = input("{} How old are you? ".format(name))

print(name)
print(age)
nacimiento = 2025 - int(age)
print(nacimiento)

print('------------')

color = input("{} What is your favorite color ?  ".format(name))
animal = input("{} What is your favorite animal?  ".format(name))
print("{}, you like a {} {}!".format(name,color,animal))
